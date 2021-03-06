#include <TMVA/Reader.h>

using namespace std;

TMVA::Reader* reader_BDTweights = new TMVA::Reader();

float mbb_var, dR_lep_w_var, dR_b_var, dphi_lep_w1_var, dR_lep_b_var, deta_lep_w1_var, dphi_lep_b1_var, dphi_met_w1_var, dphi_lep_b2_var;



void initReader()
{

    reader_BDTweights->AddVariable("mjj_b",			   &mbb_var);
    reader_BDTweights->AddVariable("deltaR_lep_wjet",              &dR_lep_w_var);
    reader_BDTweights->AddVariable("deltaR_b",                     &dR_b_var);
    reader_BDTweights->AddVariable("deltaphi_lep_wjet_high",       &dphi_lep_w1_var);
    reader_BDTweights->AddVariable("deltaR_lep_b",                 &dR_lep_b_var);
    reader_BDTweights->AddVariable("deltaeta_lep_wjet_high",       &deta_lep_w1_var);
    reader_BDTweights->AddVariable("deltaphi_lep_b_high",          &dphi_lep_b1_var);
    reader_BDTweights->AddVariable("deltaphi_met_wjet_high",       &dphi_met_w1_var);
    reader_BDTweights->AddVariable("deltaphi_lep_b_low",       	   &dphi_lep_b2_var);





    TString direction = "";
    direction = "/gwpool/users/achiapparini/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/weights_true/TMVAClassification_BDT.weights.xml";

    reader_BDTweights->BookMVA("BDT",direction);

}

Float_t BDT_var(float mjj_b,
	      float deltaR_lep_wjet,
	      float deltaR_b,
              float deltaphi_lep_wjet_high,
              float deltaR_lep_b,
              float deltaeta_lep_wjet_high,
              float deltaphi_lep_b_high,
              float deltaphi_met_wjet_high,
              float deltaphi_lep_b_low)
{
    
    mbb_var = mjj_b;
    dR_lep_w_var = deltaR_lep_wjet;
    dR_b_var = deltaR_b;
    dphi_lep_w1_var = deltaphi_lep_wjet_high;
    dR_lep_b_var = deltaR_lep_b;
    deta_lep_w1_var = deltaeta_lep_wjet_high;
    dphi_lep_b1_var = deltaphi_lep_b_high;
    dphi_met_w1_var = deltaphi_met_wjet_high;
    dphi_lep_b2_var = deltaphi_lep_b_low;


    return reader_BDTweights->EvaluateMVA("BDT");



}
