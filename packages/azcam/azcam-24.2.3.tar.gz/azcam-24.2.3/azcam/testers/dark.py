import glob
import os
import shutil

import numpy

import azcam
import azcam.utils
import azcam.fits
import azcam.image
import azcam.console.plot
from azcam.console.plot import plt
from azcam.testers.basetester import Tester


class Dark(Tester):
    """
    Dark signal acquisition and analysis.
    """

    def __init__(self):
        super().__init__("dark")

        # acquisition
        self.exposure_type = "dark"
        self.number_images_acquire = 1
        self.exposure_time = -1
        self.overscan_correct = 1  # flag to overscan correct images
        self.zero_correct = 1  # flag to correct with bias residuals

        # analysis
        self.fit_order = 3  # order of overscan correction fit

        self.use_edge_mask = False  # flag True to use defects mask

        self.mean_dark_spec = -1  # spec on mean dark signal

        self.dark_limit = -1  # spec on individual pixels
        self.dark_fraction = (
            -1
        )  # fraction of pixels required to be less than dark_limit

        self.bright_pixel_reject = -1  #  reject bright pixels e/pix/sec

        # analysis outputs
        self.num_rejected_bright_pixels = 0  # number of bright pixels rejected
        self.mean_dark_signal = -1  # mean dark signal
        self.median_dark_signal = -1  # median dark signal
        self.sdev_dark_signal = -1  # mean dark signal std
        self.dsnu = -1

        self.dark_image = []

        self.dark_fraction_measured = -1
        self.dark_rate_measured = -1
        self.means = []
        self.sdev = []
        self.hist_bins = []
        self.temperatures = []
        self.temperature = -999
        self.total_pixels = 0  # total non-masked pixels
        self.hist_values = []
        self.hist_fractions = []

        self.report_dark_per_hour = 1
        self.units_scale = 3600  # 3600 for /hr, 1 for /sec
        self.units_text = "e/pix/hr"

        # analysis output files
        self.data_file = "dark.txt"
        self.report_file = "dark"
        self.dark_filename = "dark.fits"
        self.scaled_dark_filename = "darkscaled.fits"
        self.dark_reference_filename = "darkref.fits"
        self.cumm_hist_plot = "cumm_hist.png"
        self.total_hist_plot = "total_hist.png"
        self.darkimage_plot = "darkimage.png"

        self.report_plots = ["cumm_hist", "total_hist", "darkimage"]

    def acquire(self):
        """
        Acquire dark image sets (1 sec dark, long dark) for a dark current measurement.
        NumberImages is the number of image sets to take.
        ExposureTime is the exposure time of dark image in seconds.
        """

        azcam.log("Acquiring dark sequence")

        exposure, tempcon = azcam.console.utils.get_tools(["exposure", "tempcon"])

        # save pars to be changed
        impars = {}
        azcam.db.parameters.save_imagepars(impars)

        # create new subfolder
        currentfolder, newfolder = azcam.console.utils.make_file_folder("dark")
        azcam.db.parameters.set_par("imagefolder", newfolder)

        # clear device
        exposure.test(0)

        azcam.db.parameters.set_par("imageroot", "dark.")  # for automatic data analysis
        azcam.db.parameters.set_par(
            "imageincludesequencenumber", 1
        )  # use sequence numbers
        azcam.db.parameters.set_par("imageautoname", 0)  # manually set name
        azcam.db.parameters.set_par(
            "imageautoincrementsequencenumber", 1
        )  # inc sequence numbers
        azcam.db.parameters.set_par("imagetest", 0)  # turn off TestImage

        # loop through images
        for imgnum in range(self.number_images_acquire):
            # pre-dark bias
            azcam.db.parameters.set_par("imagetype", "dark")  # for GetFilename
            filename = os.path.basename(exposure.get_filename())
            azcam.log(f"Taking pre-dark image: {filename}")
            temp = tempcon.get_temperatures()
            azcam.log(f"Current temperatures: {temp}")
            exposure.expose(0, "zero", "pre-dark bias image")

            # take dark image
            azcam.db.parameters.set_par("imagetype", "dark")
            filename = os.path.basename(exposure.get_filename())
            azcam.log(
                f"Taking dark image {imgnum + 1}/{self.number_images_acquire} for {self.exposure_time:0.3f} seconds: {filename}"
            )
            temp = tempcon.get_temperatures()
            azcam.log(f"  Current temperatures: {temp}")
            exposure.expose(self.exposure_time, "dark", "dark image")

        # finish
        azcam.db.parameters.restore_imagepars(impars)
        azcam.utils.curdir(currentfolder)
        azcam.log("Dark sequence finished")

        return

    def analyze(self):
        """
        Analyze an exisiting series zeros and darks for dark current measurement.
        """

        azcam.log("Analyzing dark signal")

        # reset filenames
        self.data_file = "dark.txt"
        self.report_file = "dark"
        self.dark_filename = "dark.fits"
        self.scaled_dark_filename = "darkscaled.fits"
        self.dark_reference_filename = "darkref.fits"
        self.cumm_hist_plot = "cumm_hist.png"
        self.darkimage_plot = "darkimage.png"

        self.temperatures = []
        self.means = []
        self.gains = []
        rootname = "dark."
        subfolder = "analysis"

        if self.report_dark_per_hour == 1:
            self.units_scale = 3600
            self.units_text = "e/pix/hr"
        else:
            self.units_scale = 1
            self.units_text = "e/pix/sec"

        # copy files to analysis subfolder
        azcam.log("Making copy of image files for analysis")
        startingfolder, subfolder = azcam.console.utils.make_file_folder(subfolder)
        for filename in glob.glob(os.path.join(startingfolder, "*.fits")):
            shutil.copy(filename, subfolder)
        currentfolder = azcam.utils.curdir(subfolder)  # move to analysis folder

        # analyze a sequence
        _, StartingSequence = azcam.console.utils.find_file_in_sequence(rootname)

        # get gain
        self.system_gain = azcam.db.tools["gain"].get_system_gain()

        # get bias image
        zerofilename = rootname + f"{StartingSequence:04d}"
        zerofilename = os.path.join(currentfolder, zerofilename) + ".fits"
        num_exts, _, _ = azcam.fits.get_extensions(zerofilename)
        self._numchans = max(1, num_exts)
        bin1 = azcam.fits.get_keyword(zerofilename, "CCDBIN1")
        bin2 = azcam.fits.get_keyword(zerofilename, "CCDBIN2")
        binned = int(bin1) * int(bin2)

        # get list of dark images
        imagelist = []
        seq = StartingSequence + 1  # pairs are bias then dark
        while True:
            df = os.path.join(currentfolder, rootname) + f"{seq:04d}.fits"
            if os.path.exists(df):
                imagelist.append(df)
                seq += 2
            else:
                break
        numdarks = len(imagelist)

        # if no overscan correct, subtract superbias from darks
        if not self.overscan_correct:
            bias = azcam.db.tools["bias"]
            for darkfile in imagelist:
                azcam.fits.sub(darkfile, bias.superbias_filename, darkfile, "uint16")

        # median combine all dark images
        masterdark = self.dark_filename
        if numdarks == 1:
            s = f"One dark image found: {imagelist[0]}"
            shutil.copyfile(imagelist[0], masterdark)
            if self.overscan_correct:
                azcam.fits.colbias(masterdark, fit_order=self.fit_order)
        else:
            azcam.fits.combine(
                imagelist,
                masterdark,
                "median",
                overscan_correct=self.overscan_correct,
                fit_order=self.fit_order,
                datatype="float32",
            )
            s = f"Number of dark images combined into {masterdark}: {numdarks}"
        azcam.log(s)

        # "debias" correct with residuals after colbias
        if self.zero_correct:
            debiased = azcam.db.tools["bias"].debiased_filename
            biassub = "biassub.fits"
            azcam.fits.sub(masterdark, debiased, biassub, "uint16")
            os.remove(masterdark)
            os.rename(biassub, masterdark)

        # create dark azcam image
        self.dark_image = azcam.image.Image(masterdark)

        # get header info
        exptime = float(azcam.fits.get_keyword(masterdark, "EXPTIME"))
        try:
            self.temperature = float(azcam.fits.get_keyword(masterdark, "CAMTEMP"))
        except Exception:
            self.temperature = -999

        # save dark reference image, bias corrected and scaled to DN per second
        azcam.fits.mult(
            masterdark, 1.0 / exptime, self.dark_reference_filename, datatype="float32"
        )

        # set scale from gain
        history = azcam.fits.get_history(masterdark)
        if "SCALED" not in history:
            azcam.log("Scale by gain values")
            self.dark_image.set_scaling(self.system_gain, None)

        # trim and assemble dark for histogram
        self.dark_image.assemble(1)

        # scale darkimage by exposure time and binning to get electrons per pixel
        self.dark_image.buffer = self.dark_image.buffer / binned / exptime

        # save scaled image
        self.dark_image.overwrite = 1
        self.dark_image.save_data_format = -32
        self.dark_image.write_file(self.scaled_dark_filename, 6)  # FITS

        # get total number of pixels image
        totalpixels = self.dark_image.buffer.shape[0] * self.dark_image.buffer.shape[1]

        # use mask from defects object (may be edge only)
        if self.use_edge_mask:
            if not azcam.db.tools["defects"].valid:
                azcam.db.tools["defects"].make_edge_mask(self.dark_image.buffer)
            self.masked_image = numpy.ma.masked_where(
                azcam.db.tools["defects"].defects_mask,
                self.dark_image.buffer,
            )
        else:
            self.masked_image = numpy.ma.masked_invalid(self.dark_image.buffer)

        # optionally mask bright pixels
        if self.bright_pixel_reject != -1:
            self.masked_image = numpy.ma.masked_where(
                self.masked_image > self.bright_pixel_reject,
                self.masked_image,
                copy=False,
            )
            self.num_rejected_bright_pixels = totalpixels - numpy.ma.count(
                self.masked_image
            )
            azcam.log(
                f"Number of rejected bright pixels: {self.num_rejected_bright_pixels}"
            )

        # get number of pixels not masked
        self.total_pixels = numpy.ma.count(self.masked_image)

        # get valid data as 1D array
        self.validdata = self.masked_image.compressed()

        self.mean_dark_signal = self.validdata.mean()
        self.sdev_dark_signal = self.validdata.std()
        self.median_dark_signal = numpy.median(self.validdata)

        # PASS or FAIL on mean dark signal if specified
        azcam.log(
            f"Mean dark signal is {(self.mean_dark_signal*self.units_scale):0.2f} {self.units_text}"
        )
        if self.median_dark_signal != -1:
            azcam.log(
                f"Median dark signal is {(self.median_dark_signal*self.units_scale):0.2f} {self.units_text}"
            )
        if self.mean_dark_spec != -1:
            if self.mean_dark_signal > self.mean_dark_spec:
                self.grade = "FAIL"
            else:
                self.grade = "PASS"
        if self.mean_dark_spec > 0:
            azcam.log(
                f"Spec for mean dark signal is {(self.mean_dark_spec*self.units_scale):0.2f} {self.units_text}"
            )

        if not self.grade_sensor:
            self.grade = "UNDEFINED"

        # report on dark signal historgram if dark_fraction specified
        if self.dark_fraction != -1:
            ordered = sorted(self.validdata)
            max1 = int(len(ordered) * self.dark_fraction)
            trimmed = ordered[:max1]
            self.dark_rate_measured = max(trimmed)
            s1 = f"{self.dark_fraction * 100:0.1f}% of pixels are below {(self.dark_rate_measured*self.units_scale):0.2f} {self.units_text}"
            azcam.log(s1)
            azcam.log(
                f"Spec is {100.*self.dark_fraction:0.1f}% below {(self.dark_limit*self.units_scale)} {self.units_text}"
            )

        azcam.log(f"Grade = {self.grade}")

        if self.create_plots:
            self.plot()

        # copy processed dark file starting folder
        if startingfolder != subfolder:
            shutil.copy(os.path.abspath(self.dark_filename), startingfolder)
            shutil.copy(os.path.abspath(self.scaled_dark_filename), startingfolder)
            shutil.copy(os.path.abspath(self.dark_reference_filename), startingfolder)
            if self.create_plots:
                shutil.copy(os.path.abspath(self.darkimage_plot), startingfolder)
                shutil.copy(os.path.abspath(self.cumm_hist_plot), startingfolder)
                shutil.copy(os.path.abspath(self.total_hist_plot), startingfolder)

        # set absolute filenames
        azcam.utils.curdir(startingfolder)
        self.dark_filename = os.path.abspath(self.dark_filename)
        self.scaled_dark_filename = os.path.abspath(self.scaled_dark_filename)
        self.dark_reference_filename = os.path.abspath(self.dark_reference_filename)
        self.darkimage_plot = os.path.abspath(self.darkimage_plot)
        self.cumm_hist_plot = os.path.abspath(self.cumm_hist_plot)

        # define dataset
        self.dataset = {
            "data_file": self.data_file,
            "grade": self.grade,
            "temperature": self.temperature,
            "total_pixels": float(self.total_pixels),
            "mean_dark_signal": float(self.mean_dark_signal),
            "dark_fraction_measured": float(self.dark_fraction_measured),
            "dark_rate_measured": float(self.dark_rate_measured),
            "hist_bins": numpy.array(self.hist_bins).tolist(),
            "hist_fractions": numpy.array(self.hist_fractions).tolist(),
            "hist_values": numpy.array(self.hist_values).tolist(),
            # "dsnu": numpy.array(self.dsnu).tolist(),
        }

        # write output files
        self.write_datafile()
        if self.create_reports:
            self.report()

        # finish
        self.valid = True

        return

    def plot(self):
        """
        Plot analysis results.
        """

        if self._numchans == 1:
            plotconfig = (1, 1)
        elif self._numchans == 2:
            plotconfig = (1, 2)
        elif self._numchans == 4:
            plotconfig = (2, 2)
        else:
            raise azcam.AzcamError("missing subplot configuration")

        # plot dark image
        fig = plt.figure()
        fignum = fig.number
        azcam.console.plot.move_window(fignum)
        azcam.console.plot.plot_image(self.dark_image, "sdev", 10.0)
        plt.title("Combined Dark Image")
        plt.show()
        azcam.console.plot.save_figure(fignum, self.darkimage_plot)

        for chan in range(self._numchans):
            # plt.subplot(plotconfig[0], plotconfig[1], chan + 1)
            # ax = plt.gca()

            min1 = self.dark_image.data[chan].min()
            max1 = self.dark_image.data[chan].max()
            counts, bins = numpy.histogram(
                self.dark_image.data[chan], int(max1) - int(min1) + 1, density=True
            )
            step = bins[1] - bins[0]
            self.counts = counts
            self.bins = bins

        # plot cummulative histogram
        fig = plt.figure()
        fignum = fig.number
        azcam.console.plot.move_window(fignum)
        plt.hist(
            (self.validdata * self.units_scale),
            bins="auto",
            density=True,
            histtype="step",
            cumulative=True,
        )
        ax = plt.gca()
        ax.set_xlabel(f"Dark Signal [{self.units_text}]")
        ax.set_ylabel("Fraction")

        if self.temperature != -999:
            labels = [f"Mean Temp = {self.temperature:.1f} C"]
            ax.annotate(
                labels[0],
                xy=(0.65, 0.95),
                xycoords="axes fraction",
                horizontalalignment="left",
                verticalalignment="top",
            )

        if self.mean_dark_spec > 0:
            plt.axvline(
                x=self.mean_dark_spec * self.units_scale,
                linestyle="dashed",
                color="red",
                label="Mean spec",
            )

        plt.axvline(
            x=self.mean_dark_signal * self.units_scale,
            linestyle="solid",
            color="red",
            label="Mean",
        )

        if self.median_dark_signal > 0:
            plt.axvline(
                x=self.median_dark_signal * self.units_scale,
                linestyle="dashdot",
                color="black",
                label="Median",
            )

        if self.dark_limit > 0:
            plt.axhline(
                y=self.dark_fraction, linestyle="--", color="red", label="Fraction"
            )
            plt.axvline(
                x=self.dark_limit * self.units_scale,
                linestyle="--",
                color="blue",
                label="Limit",
            )
        plt.legend(loc="lower right")
        plt.title("Dark Signal Cummulative Histogram")
        plt.xlim(
            [
                0,
                self.mean_dark_signal * 3 * self.units_scale,
            ]
        )
        plt.show()
        azcam.console.plot.save_figure(fignum, self.cumm_hist_plot)

        # plot total histogram
        fig = plt.figure()
        fignum = fig.number
        azcam.console.plot.move_window(fignum)
        plt.hist(
            (self.validdata * self.units_scale),
            bins="auto",
            density=1,
            histtype="step",
            cumulative=False,
        )
        ax = plt.gca()
        ax.set_xlabel(f"Dark Signal [{self.units_text}]")
        ax.set_ylabel("Pixel Fraction")
        plt.xlim(
            [
                0,
                self.mean_dark_signal * 3 * self.units_scale,
            ]
        )
        plt.title("Dark Signal Histogram")
        plt.show()
        azcam.console.plot.save_figure(fignum, self.total_hist_plot)

        return

    def report(self):
        """
        Write report file.
        """

        lines = ["# Dark Signal Analysis", ""]

        if self.grade != "UNDEFINED":
            s = f"Dark signal grade = {self.grade}  "
            lines.append(s)

        if self.dark_fraction > 0:
            s = f"{self.dark_fraction_measured * 100:0.1f} of pixels are below {(self.dark_rate_measured*self.units_scale):0.3f} {self.units_text}  "
            lines.append(s)

        s = f"Mean dark signal is {self.units_scale*self.mean_dark_signal:0.2f} {self.units_text}  "
        lines.append(s)
        if self.mean_dark_spec > 0:
            s = f"Dark signal spec is {self.units_scale*self.mean_dark_spec:0.2f} {self.units_text}  "
            lines.append(s)

        s = f"Median dark signal is {self.units_scale*self.median_dark_signal:0.2f} {self.units_text}  "
        lines.append(s)

        # if self.dsnu > 0:
        #     s = f"Dark signal non-uniformity is {100. * self.units_scale*self.dsnu:0.2f}% {self.units_text}  "
        #     lines.append(s)

        lines.append("")
        if "cumm_hist" in self.report_plots:
            lines.append(
                f"![Cumulative Histogram]({os.path.abspath(self.cumm_hist_plot)})  "
            )
            lines.append("*Cumulative Dark Signal Histogram.*")
            lines.append("")

        if "total_hist" in self.report_plots:
            lines.append(
                f"![Total Histogram]({os.path.abspath(self.total_hist_plot)})  "
            )
            lines.append("*Total Dark Signal Histogram.*")
            lines.append("")

        if "darkimage" in self.report_plots:
            lines.append(f"![Dark Image]({os.path.abspath(self.darkimage_plot)})  ")
            lines.append("*Dark Image.*")
            lines.append("")

        # Make report files
        self.write_report(self.report_file, lines)

        return
