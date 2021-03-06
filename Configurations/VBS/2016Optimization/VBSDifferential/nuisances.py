nuisances={}

##############################################
nuisances['lumi2016']={
    "name": "lumi_13TeV_2016",
    "samples": {
        "ChMisId": "1.025",
        "Vg": "1.025",
        "ttbar": "1.025",
        "ZZ": "1.025",
        "VVV": "1.025",
        "DPS": "1.025",
        "WW_strong": "1.025",
        "Signal_bin0": "1.025",
        "Signal_bin1": "1.025",
        "Signal_bin2": "1.025",
        "Signal_bin3": "1.025",
        "Signal_bin4": "1.025"
    },
    "type": "lnN"
}

nuisances['QCDscale']={
    "name": "QCDscale",
    "type": "lnN",
    "samples": {
        "ChMisId": "1.10",
        "ttbar": "1.10",
        "WZ": "1.10",
        "ZZ": "1.10",
        "VVV": "1.10",
        "DPS": "1.10",
        "Vg": "1.10",
        "WW_strong": "1.10",
        "Signal_bin0": "1.10",
        "Signal_bin1": "1.10",
        "Signal_bin2": "1.10",
        "Signal_bin3": "1.10",
        "Signal_bin4": "1.10"
    }
}

nuisances['QCDscale_gg_accept']={
    "name": "QCDscale_gg_accept",
    "type": "lnN",
    "samples": {
        "DY": "0.976/1.012",
        "WW_strong": "1.01",
        "Signal_bin0": "1.01",
        "Signal_bin1": "1.01",
        "Signal_bin2": "1.01",
        "Signal_bin3": "1.01",
        "Signal_bin4": "1.01"
    }
}

nuisances['QCDscale_qqbar_accept']={
    "name": "QCDscale_qqbar_accept",
    "type": "lnN",
    "samples": {
        "lep_TT": "0.974/1.005",
        "Vg": "0.949/1.008"
    }
}

nuisances['pdf']={
    "name": "pdf",
    "type": "lnN",
    "samples": {
        "ChMisId": "1.01",
        "ttbar": "1.01",
        "WZ": "1.01",
        "ZZ": "1.01",
        "VVV": "1.01",
        "DPS": "1.01",
        "Vg": "1.01",
        "WW_strong": "1.01",
        "Signal_bin0": "1.01",
        "Signal_bin1": "1.01",
        "Signal_bin2": "1.01",
        "Signal_bin3": "1.01",
        "Signal_bin4": "1.01"
    }
}

nuisances['WZ_norm']={
    "name": "WZ_norm",
    "samples": {
        "WZ": "1.3"
    },
    "type": "lnN"
}

nuisances['charge_flip']={
    "name": "charge_flip",
    "samples": {
        "ChMisId": "1.07",
        "ttbar": "1.07"
    },
    "type": "lnN"
}

nuisances['fake_syst']={
    "name": "fake_syst",
    "type": "lnN",
    "samples": {
        "Fake_lep": "1.30"
    }
}

nuisances['btagbc']={
    "name": "ICHEP_btag_bc",
    "kind": "weight",
    "type": "shape",
    "samples": {
        "ChMisId": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "ttbar": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "Vg": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "WZ": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "ZZ": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "VVV": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "DPS": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "WW_strong": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "Signal_bin0": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "Signal_bin1": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "Signal_bin2": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "Signal_bin3": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ],
        "Signal_bin4": [
            "(bPogSF_CSVM_bc_up)/(bPogSF)",
            "(bPogSF_CSVM_bc_down)/(bPogSF)"
        ]
    }
}

nuisances['btagudsg']={
    "name": "ICHEP_btag_udsg",
    "kind": "weight",
    "type": "shape",
    "samples": {
        "ChMisId": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "ttbar": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "Vg": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "WZ": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "ZZ": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "VVV": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "DPS": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "WW_strong": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "Signal_bin0": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "Signal_bin1": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "Signal_bin2": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "Signal_bin3": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ],
        "Signal_bin4": [
            "(bPogSF_CSVM_udsg_up)/(bPogSF)",
            "(bPogSF_CSVM_udsg_down)/(bPogSF)"
        ]
    }
}

nuisances['trigg']={
    "name": "trigger",
    "kind": "weight",
    "type": "shape",
    "samples": {
        "ChMisId": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "ttbar": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "Vg": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "WZ": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "ZZ": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "VVV": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "DPS": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "WW_strong": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "Signal_bin0": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "Signal_bin1": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "Signal_bin2": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "Signal_bin3": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ],
        "Signal_bin4": [
            "(effTrigW_Up)/(effTrigW)",
            "(effTrigW_Down)/(effTrigW)"
        ]
    }
}

nuisances['idiso_ele']={
    "name": "idiso_ele",
    "kind": "weight",
    "type": "shape",
    "samples": {
        "ChMisId": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "ttbar": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "Vg": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "WZ": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "ZZ": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "VVV": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "DPS": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "WW_strong": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "Signal_bin0": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "Signal_bin1": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "Signal_bin2": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "Signal_bin3": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ],
        "Signal_bin4": [
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))",
            "((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))"
        ]
    }
}

nuisances['idiso_mu']={
    "name": "idiso_mu",
    "kind": "weight",
    "type": "shape",
    "samples": {
        "ChMisId": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "ttbar": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "Vg": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "WZ": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "ZZ": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "VVV": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "DPS": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "WW_strong": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "Signal_bin0": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "Signal_bin1": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "Signal_bin2": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "Signal_bin3": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ],
        "Signal_bin4": [
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))",
            "((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))"
        ]
    }
}

nuisances['jes']={
    "name": "scale_j",
    "kind": "tree",
    "type": "shape",
    "samples": {
        "ChMisId": [
            "1",
            "1"
        ],
        "ttbar": [
            "1",
            "1"
        ],
        "Vg": [
            "1",
            "1"
        ],
        "WZ": [
            "1",
            "1"
        ],
        "ZZ": [
            "1",
            "1"
        ],
        "VVV": [
            "1",
            "1"
        ],
        "DPS": [
            "1",
            "1"
        ],
        "WW_strong": [
            "1",
            "1"
        ],
        "Signal_bin0": [
            "1",
            "1"
        ],
        "Signal_bin1": [
            "1",
            "1"
        ],
        "Signal_bin2": [
            "1",
            "1"
        ],
        "Signal_bin3": [
            "1",
            "1"
        ],
        "Signal_bin4": [
            "1",
            "1"
        ]
    },
    "folderUp": "/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__JESup__tightVbsSel/",
    "folderDown": "/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__JESdo__tightVbsSel/"
}

nuisances['electronpt']={
    "name": "scale_e",
    "kind": "tree",
    "type": "shape",
    "samples": {
        "ChMisId": [
            "1",
            "1"
        ],
        "ttbar": [
            "1",
            "1"
        ],
        "Vg": [
            "1",
            "1"
        ],
        "WZ": [
            "1",
            "1"
        ],
        "ZZ": [
            "1",
            "1"
        ],
        "VVV": [
            "1",
            "1"
        ],
        "DPS": [
            "1",
            "1"
        ],
        "WW_strong": [
            "1",
            "1"
        ],
        "Signal_bin0": [
            "1",
            "1"
        ],
        "Signal_bin1": [
            "1",
            "1"
        ],
        "Signal_bin2": [
            "1",
            "1"
        ],
        "Signal_bin3": [
            "1",
            "1"
        ],
        "Signal_bin4": [
            "1",
            "1"
        ]
    },
    "folderUp": "/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepElepTCutup__tightVbsSel/",
    "folderDown": "/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepElepTCutdo__tightVbsSel/"
}

nuisances['muonpt']={
    "name": "scale_m",
    "kind": "tree",
    "type": "shape",
    "samples": {
        "ChMisId": [
            "1",
            "1"
        ],
        "ttbar": [
            "1",
            "1"
        ],
        "Vg": [
            "1",
            "1"
        ],
        "WZ": [
            "1",
            "1"
        ],
        "ZZ": [
            "1",
            "1"
        ],
        "VVV": [
            "1",
            "1"
        ],
        "DPS": [
            "1",
            "1"
        ],
        "WW_strong": [
            "1",
            "1"
        ],
        "Signal_bin0": [
            "1",
            "1"
        ],
        "Signal_bin1": [
            "1",
            "1"
        ],
        "Signal_bin2": [
            "1",
            "1"
        ],
        "Signal_bin3": [
            "1",
            "1"
        ],
        "Signal_bin4": [
            "1",
            "1"
        ]
    },
    "folderUp": "/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepMupTCutup__tightVbsSel/",
    "folderDown": "/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepMupTCutdo__tightVbsSel/"
}

nuisances['met']={
    "name": "scale_met",
    "kind": "tree",
    "type": "shape",
    "samples": {
        "ChMisId": [
            "1",
            "1"
        ],
        "ttbar": [
            "1",
            "1"
        ],
        "Vg": [
            "1",
            "1"
        ],
        "WZ": [
            "1",
            "1"
        ],
        "ZZ": [
            "1",
            "1"
        ],
        "VVV": [
            "1",
            "1"
        ],
        "DPS": [
            "1",
            "1"
        ],
        "WW_strong": [
            "1",
            "1"
        ],
        "Signal_bin0": [
            "1",
            "1"
        ],
        "Signal_bin1": [
            "1",
            "1"
        ],
        "Signal_bin2": [
            "1",
            "1"
        ],
        "Signal_bin3": [
            "1",
            "1"
        ],
        "Signal_bin4": [
            "1",
            "1"
        ]
    },
    "folderUp": "/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__METup__tightVbsSel/",
    "folderDown": "/gwteras/cms/store/group/OneLepton/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__METdo__tightVbsSel/"
}

nuisances['stat']={
    "type": "auto",
    "maxPoiss": "10",
    "includeSignal": "1",
    "samples": {}
}


