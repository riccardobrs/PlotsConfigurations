import os
import sys
import collections
import array
import ROOT
import root_numpy

import common

confdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

ntemplate = ROOT.TH1D('ntemplate', '', 4, 0., 4.) # ptH indiv, njet indiv, ptH comb, njet comb

canvas = ROOT.TCanvas('c1', 'c1', 600, 600)
canvas.SetGridy(True)
canvas.SetLeftMargin(0.15)
canvas.SetRightMargin(0.05)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.05)

colors = {
    '2016': ROOT.kRed + 2,
    '2017': ROOT.kGreen + 2,
    '2018': ROOT.kBlue + 2,
    'combination': ROOT.kBlack
}

postfit_norms = {}

for proc in ['WW', 'top', 'DY']:
    for dataset in ['2016', '2017', '2018']:
        postfit_norms[(dataset, proc)] = ntemplate.Clone('postfit_norms_%s_%s' % (dataset, proc))

for observable in ['ptH', 'njet']:
    prefit_rnorms = {}
    postfit_rnorms = {}
    postfit_rates = {}
    
    binnames = common.binnames[observable]
    bintitles = common.bintitles[observable]
    if observable == 'ptH':
        xtitle = 'p_{T}^{H} (GeV)'
    else:
        xtitle = 'N_{jet}'

    template = ROOT.TH1D('template', '', len(binnames), 0., float(len(binnames)))
    template.Sumw2()
    
    for fit in ['2016', '2017', '2018', 'combination']:
        for proc in ['WW', 'top', 'DY']:
            prefit_rnorms[(fit, proc)] = template.Clone('prefit_rnorms_%s_%s' % (fit, proc))
            postfit_rnorms[(fit, proc)] = template.Clone('postfit_rnorms_%s_%s' % (fit, proc))
            postfit_rates[(fit, proc)] = template.Clone('postfit_rates_%s_%s' % (fit, proc))

        if observable == 'ptH':
            normbin = 1
        else:
            normbin = 2
        if fit == 'combination':
            normbin += 2
    
        if fit == 'combination':
            source = ROOT.TFile.Open('%s/combination/%s_fullmodel/higgsCombineUnreg.MultiDimFit.mH120.root' % (confdir, observable))
        else:
            source = ROOT.TFile.Open('%s/ggH%s/merged_cards/%s_fullmodel/higgsCombineUnreg.MultiDimFit.mH120.root' % (confdir, fit, observable))
    
        w = source.Get('w')
        
        model = w.pdf('model_s')
        categories = model.indexCat().Clone()
    
        for proc in ['WW', 'top', 'DY']:
            hist = prefit_rnorms[(fit, proc)]
    
            for index in range(categories.numBins('')):
                categories.setBin(index)
                cat = categories.getLabel()
        
                if '_CR_' in cat:
                    continue

                # we don't really need the histogram but whatever
                h = common.make_roofit_histogram(w, cat, proc, 'temp')
                if h is None:
                    continue

                n = h.GetSumOfWeights()
                h.Delete()
    
                if fit == 'combination':
                    bin = cat[12:]
                else:
                    bin = cat[4:]
    
                bin = bin[:bin.rfind('_')] # remove the year
    
                if '_cat' in bin:
                    bin = bin[:bin.find('_cat')]
    
                ibin = binnames.index(bin)
    
                hist.SetBinContent(ibin + 1, hist.GetBinContent(ibin + 1) + n)
    
        w.loadSnapshot('MultiDimFit')
    
        for proc in ['WW', 'top', 'DY']:
            hist = postfit_rnorms[(fit, proc)]
   
            for index in range(categories.numBins('')):
                categories.setBin(index)
                cat = categories.getLabel()
        
                if '_CR_' in cat:
                    continue

                # we don't really need the histogram but whatever
                h = common.make_roofit_histogram(w, cat, proc, 'temp')
                if h is None:
                    continue

                n = h.GetSumOfWeights()
                h.Delete()

                print observable, fit, 'n_exp_final_bin%s_proc_%s' % (cat, proc), n
    
                if fit == 'combination':
                    bin = cat[12:]
                else:
                    bin = cat[4:]
    
                dataset = bin[bin.rfind('_') + 1:]
    
                bin = bin[:bin.rfind('_')] # remove the year
    
                if '_cat' in bin:
                    bin = bin[:bin.find('_cat')]
    
                ibin = binnames.index(bin)
    
                hist.SetBinContent(ibin + 1, hist.GetBinContent(ibin + 1) + n)
    
                nhist = postfit_norms[(dataset, proc)]
                nhist.SetBinContent(normbin, nhist.GetBinContent(normbin) + n)
    
            hist.Divide(prefit_rnorms[(fit, proc)])
            for ix in range(1, hist.GetNbinsX() + 1):
                if prefit_rnorms[(fit, proc)].GetBinContent(ix) == 0.:
                    hist.SetBinContent(ix, -10.)
    
            # give a small uncert so that EP renders a line
            err = root_numpy.array(hist.GetSumw2(), copy=False)
            err[:] = 1.e-6
    
            hist = postfit_rates[(fit, proc)]
    
            for ibin, bin in enumerate(binnames):
                rate = w.var('CMS_hww_%snorm_%s' % (proc, bin))
                hist.SetBinContent(ibin + 1, rate.getVal())
                if rate.getError() == 0.:
                    hist.SetBinError(ibin + 1, 1.e-3)
                else:
                    hist.SetBinError(ibin + 1, rate.getError())
    
        source.Close()
   
    for name, hists in [('rnorm', postfit_rnorms), ('rate', postfit_rates)]:
        for proc in ['WW', 'top', 'DY']:
            legend = ROOT.TLegend(0.17, 0.17, 0.4, 0.4)
            legend.SetFillStyle(0)
            legend.SetBorderSize(0)
    
            drawopt = 'EP'
            for fit in ['2016', '2017', '2018', 'combination']:
                hist = hists[(fit, proc)]
                hist.SetLineColor(colors[fit])
                hist.SetMarkerColor(colors[fit])
                hist.SetLineWidth(2)
                hist.SetMarkerSize(0)
                if fit != 'combination':
                    hist.SetLineStyle(ROOT.kDashed)
    
                if drawopt == 'EP':
                    hist.SetMinimum(0.)
                    hist.SetMaximum(2.)
                    hist.GetXaxis().SetTitle(xtitle)
                    hist.GetYaxis().SetTitle('Postfit / prefit')
                    for ibin, title in enumerate(bintitles):
                        hist.GetXaxis().SetBinLabel(ibin + 1, title)
        
                hist.Draw(drawopt)
                drawopt = 'EP SAME'
                
                legend.AddEntry(hist, fit, 'LP')
    
            legend.Draw()
    
            canvas.Print('%s_%s_%s.png' % (observable, name, proc))
            canvas.Print('%s_%s_%s.pdf' % (observable, name, proc))

canvas.SetGridy(False)

for proc in ['WW', 'top', 'DY']:
    for dataset in ['2016', '2017', '2018']:
        nhist = postfit_norms[(dataset, proc)]
        nhist.SetMinimum(0.)
        nhist.SetLineColor(ROOT.kBlack)
        nhist.SetLineWidth(2)
        nhist.GetXaxis().SetBinLabel(1, 'ptH %s' % dataset)
        nhist.GetXaxis().SetBinLabel(2, 'njet %s' % dataset)
        nhist.GetXaxis().SetBinLabel(3, 'ptH combined')
        nhist.GetXaxis().SetBinLabel(4, 'njet combined')

        nhist.Draw('HIST')
        canvas.Print('postfitnorm_%s_%s.png' % (dataset, proc))
        canvas.Print('postfitnorm_%s_%s.pdf' % (dataset, proc))
