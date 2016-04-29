#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Mar  8 19:50:00 2016
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000000
        self.freq_slider_0 = freq_slider_0 = 93.6
        self.radio_freq = radio_freq = freq_slider_0*1e6
        self.offset_freq = offset_freq = -100000
        self.filter_taps2 = filter_taps2 = [1]
        self.filter_taps1 = filter_taps1 = firdes.low_pass(1,samp_rate,100000,1000,firdes.WIN_HAMMING)

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=48000,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=48000,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=True,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=6,
                decimation=25,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, 200000, 16000, 2000, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(5, (filter_taps1), offset_freq, samp_rate)
        _freq_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_slider_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_slider_0_sizer,
        	value=self.freq_slider_0,
        	callback=self.set_freq_slider_0,
        	label='freq_slider_0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_slider_0_sizer,
        	value=self.freq_slider_0,
        	callback=self.set_freq_slider_0,
        	minimum=88,
        	maximum=108,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_slider_0_sizer)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "Documents/gnuradio/cap.cpx", True)
        self.blks2_valve_0 = grc_blks2.valve(item_size=gr.sizeof_float*1, open=bool(0))
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=200000,
        	audio_decimation=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blks2_valve_0, 0), (self.wxgui_waterfallsink2_0, 0))
        self.connect((self.blks2_valve_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blks2_valve_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_filter_taps1(firdes.low_pass(1,self.samp_rate,100000,1000,firdes.WIN_HAMMING))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_freq_slider_0(self):
        return self.freq_slider_0

    def set_freq_slider_0(self, freq_slider_0):
        self.freq_slider_0 = freq_slider_0
        self.set_radio_freq(self.freq_slider_0*1e6)
        self._freq_slider_0_slider.set_value(self.freq_slider_0)
        self._freq_slider_0_text_box.set_value(self.freq_slider_0)

    def get_radio_freq(self):
        return self.radio_freq

    def set_radio_freq(self, radio_freq):
        self.radio_freq = radio_freq

    def get_offset_freq(self):
        return self.offset_freq

    def set_offset_freq(self, offset_freq):
        self.offset_freq = offset_freq
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.offset_freq)

    def get_filter_taps2(self):
        return self.filter_taps2

    def set_filter_taps2(self, filter_taps2):
        self.filter_taps2 = filter_taps2

    def get_filter_taps1(self):
        return self.filter_taps1

    def set_filter_taps1(self, filter_taps1):
        self.filter_taps1 = filter_taps1
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.filter_taps1))

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

