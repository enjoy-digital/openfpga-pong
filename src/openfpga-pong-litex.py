#!/usr/bin/env python3

#
# LiteX wrapper around OpenFPGA-Pong.
#
# Copyright (c) 2023 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause
#
# OpenFPGA-Pong is MIT Licensed / Copyright (c) 2022 Adam Gastineau.

from litex.gen import *

from litex_boards.platforms import analog_pocket

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCMini):
    def __init__(self, sys_clk_freq=50e6, **kwargs):
        platform = analog_pocket.Platform(ios="analog")

        # CRG --------------------------------------------------------------------------------------
        self.cd_sys = ClockDomain() # FIXME: Not connected.

        # SoCMini ----------------------------------------------------------------------------------
        SoCMini.__init__(self, platform, sys_clk_freq, ident="LiteX Wrapper around OpenFPGA-Pong")

        # APF Top ----------------------------------------------------------------------------------

        # APF Top Pads.
        # -------------
        cart      = platform.request("cart")
        port_ir   = platform.request("port_ir")
        port_tran = platform.request("port_tran")
        scal      = platform.request("scal")
        bridge    = platform.request("bridge")
        cram0     = platform.request("cram0")
        cram1     = platform.request("cram1")
        dram      = platform.request("dram")
        sram      = platform.request("sram")
        vblank    = platform.request("vblank")
        dbg_tx    = platform.request("dbg_tx")
        dbg_rx    = platform.request("dbg_rx")
        user1     = platform.request("user1")
        user2     = platform.request("user2")
        bist      = platform.request("bist")
        vpll_feed = platform.request("vpll_feed")
        aux_sda   = platform.request("aux_sda")
        aux_scl   = platform.request("aux_scl")

        # APF Top Instance.
        # -----------------
        self.specials += Instance("apf_top",
            # Clk.
            # ----
            i_clk_74a = platform.request("clk_74a"),
            i_clk_74b = platform.request("clk_74b"),

            # Cart.
            # -----
            io_cart_tran_bank2        = cart.tran_bank2,
            o_cart_tran_bank2_dir     = cart.tran_bank2_dir,
            io_cart_tran_bank3        = cart.tran_bank3,
            o_cart_tran_bank3_dir     = cart.tran_bank3_dir,
            io_cart_tran_bank1        = cart.tran_bank1,
            o_cart_tran_bank1_dir     = cart.tran_bank1_dir,
            io_cart_tran_bank0        = cart.tran_bank0,
            o_cart_tran_bank0_dir     = cart.tran_bank0_dir,
            io_cart_tran_pin30        = cart.tran_pin30,
            o_cart_tran_pin30_dir     = cart.tran_pin30_dir,
            o_cart_pin30_pwroff_reset = cart.pin30_pwroff_reset,
            io_cart_tran_pin31        = cart.tran_pin31,
            o_cart_tran_pin31_dir     = cart.tran_pin31_dir,

            # IR.
            # ---
            i_port_ir_rx         = port_ir.rx,
            o_port_ir_tx         = port_ir.tx,
            o_port_ir_rx_disable = port_ir.rx_disable,

            # Port Tran.
            # ----------
            io_port_tran_si     = port_tran.si,
            o_port_tran_si_dir  = port_tran.si_dir,
            io_port_tran_so     = port_tran.so,
            o_port_tran_so_dir  = port_tran.so_dir,
            io_port_tran_sck    = port_tran.sck,
            o_port_tran_sck_dir = port_tran.sck_dir,
            io_port_tran_sd     = port_tran.sd,
            o_port_tran_sd_dir  = port_tran.sd_dir,

            # Scaler.
            # -------
            io_scal_vid    = scal.vid,
            io_scal_clk    = scal.clk,
            io_scal_de     = scal.de,
            io_scal_skip   = scal.skip,
            io_scal_vs     = scal.vs,
            io_scal_hs     = scal.hs,
            o_scal_audmclk = scal.audmclk,
            i_scal_audadc  = scal.audadc,
            o_scal_auddac  = scal.auddac,
            o_scal_audlrck = scal.audlrck,

            # Bridge.
            # -------
            io_bridge_spimosi = bridge.spimosi,
            io_bridge_spimiso = bridge.spimiso,
            io_bridge_spiclk  = bridge.spiclk,
            i_bridge_spiss    = bridge.spiss,
            io_bridge_1wire   = bridge.lwire,

            # CRAM0.
            # ------
            o_cram0_a     = cram0.a,
            io_cram0_dq   = cram0.dq,
            i_cram0_wait  = cram0.wait,
            o_cram0_clk   = cram0.clk,
            o_cram0_adv_n = cram0.adv_n,
            o_cram0_cre   = cram0.cre,
            o_cram0_ce0_n = cram0.ce0_n,
            o_cram0_ce1_n = cram0.ce1_n,
            o_cram0_oe_n  = cram0.oe_n,
            o_cram0_we_n  = cram0.we_n,
            o_cram0_ub_n  = cram0.ub_n,
            o_cram0_lb_n  = cram0.lb_n,

            # CRAM1.
            # ------
            o_cram1_a     = cram1.a,
            io_cram1_dq   = cram1.dq,
            i_cram1_wait  = cram1.wait,
            o_cram1_clk   = cram1.clk,
            o_cram1_adv_n = cram1.adv_n,
            o_cram1_cre   = cram1.cre,
            o_cram1_ce0_n = cram1.ce0_n,
            o_cram1_ce1_n = cram1.ce1_n,
            o_cram1_oe_n  = cram1.oe_n,
            o_cram1_we_n  = cram1.we_n,
            o_cram1_ub_n  = cram1.ub_n,
            o_cram1_lb_n  = cram1.lb_n,

            # DRAM.
            # -----
            o_dram_a     = dram.a,
            o_dram_ba    = dram.ba,
            io_dram_dq   = dram.dq,
            o_dram_dqm   = dram.dqm,
            o_dram_clk   = dram.clk,
            o_dram_cke   = dram.cke,
            o_dram_ras_n = dram.ras_n,
            o_dram_cas_n = dram.cas_n,
            o_dram_we_n  = dram.we_n,

            # SRAM.
            # -----
            o_sram_a    = sram.a,
            io_sram_dq  = sram.dq,
            o_sram_oe_n = sram.oe_n,
            o_sram_we_n = sram.we_n,
            o_sram_ub_n = sram.ub_n,
            o_sram_lb_n = sram.lb_n,

            # Others (FIXME: Cleanup).
            # ------------------------
            i_vblank    = vblank,
            o_dbg_tx    = dbg_tx,
            i_dbg_rx    = dbg_rx,
            o_user1     = user1,
            i_user2     = user2,
            io_bist     = bist,
            o_vpll_feed = vpll_feed,
            io_aux_sda  = aux_sda,
            o_aux_scl   = aux_scl,
        )

        # APF Sources.
        # ------------
        platform.add_source_dir("fpga/apf",             recursive=False)

        # Core Sources.
        # -------------
        platform.add_source_dir("fpga/core",            recursive=False)
        platform.add_source_dir("fpga/core/mf_pllbase", recursive=False)
        platform.add_source_dir("fpga/core/pong",       recursive=False)
        platform.add_source_dir("fpga/core/pong/ball",  recursive=False)
        platform.add_source_dir("fpga/core/pong/ic",    recursive=False)
        platform.add_source_dir("fpga/core/pong/score", recursive=False)
        platform.add_source_dir("fpga/core/pong/video", recursive=False)

        # Build Parameters.
        # -----------------
        platform.add_platform_command("set_global_assignment -name VHDL_INPUT_VERSION VHDL_2008")
        platform.add_platform_command("set_global_assignment -name VHDL_SHOW_LMF_MAPPING_MESSAGES OFF")

# Build --------------------------------------------------------------------------------------------

def main():
    from litex.build.parser import LiteXArgumentParser
    parser = LiteXArgumentParser(platform=analog_pocket.Platform, description="Pong on Analog Pocket.")
    args = parser.parse_args()

    soc = BaseSoC(
        **parser.soc_argdict
    )
    builder = Builder(soc, **parser.builder_argdict)
    if args.build:
        builder.build(**parser.toolchain_argdict)

    if args.load:
        prog = soc.platform.create_programmer()
        prog.load_bitstream(builder.get_bitstream_filename(mode="sram").replace(".sof", ".rbf"))

if __name__ == "__main__":
    main()
