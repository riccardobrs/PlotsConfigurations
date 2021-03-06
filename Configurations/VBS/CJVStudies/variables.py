# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['mll']  = {   'name': 'mll',            #   variable name
                       'range' : (20, 0. ,600),    #15   variable range
                       'xaxis' : 'mll [GeV]',  #   x axis name
                       'fold' : 3
                       }

#dynamic JV bin = 80
'''
variables['djv_ptl1']  = {   'name': '(std_vector_jet_pt[2]>20)*(std_vector_jet_pt[2]/std_vector_lepton_pt[0])+(!(std_vector_jet_pt[2]>20))*(-9999/std_vector_lepton_pt[0])',
                       'range' : (80, 0 ,2), #(12, -0.41 ,2) (10, -1 ,2)  #25bin
                       'xaxis' : 'p_{t} jet3 / p_{t}^{lep1}',  
                       'fold' : 1,
                       'SignalOnRight' : -1
                       } #usually jet_pt > 20 (if not verified, use 0 instead of jet_pt)
variables['djv_ptll']  = {   'name': '(std_vector_jet_pt[2]>20)*(std_vector_jet_pt[2]/ptll)+(!(std_vector_jet_pt[2]>20))*(-9999/ptll)',
                       'range' : (80, 0 ,2), #(10, -1 ,2)  
                       'xaxis' : 'p_{t} jet3 / p_{t}^{ll}',  
                       'fold' : 1,
                       'SignalOnRight' : -1
                       } #usually jet_pt > 20 (if not verified, use 0 instead of jet_pt)
variables['djv_mll']  = {   'name': '(std_vector_jet_pt[2]>20)*(std_vector_jet_pt[2]/mll)+(!(std_vector_jet_pt[2]>20))*(-9999/mll)',
                       'range' : (80, 0 ,2),  #25bin  (25, 0 ,2)
                       'xaxis' : 'p_{t} jet3 / m_{ll}',
                       'fold' : 1,
                       'SignalOnRight' : -1
                       } #usually jet_pt > 20 (if not verified, use 0 instead of jet_pt)
'''
'''
variables['djv_mjj']  = {   'name': '(std_vector_jet_pt[2]>20)*(std_vector_jet_pt[2]/mjj)+(!(std_vector_jet_pt[2]>20))*(-9999/mjj)',
                       'range' : (80, 0 ,0.18), # (22,-0.018,0.18)  
                       'xaxis' : 'p_{t} jet3 / m_{jj}',
                       'fold' : 1,
                       'SignalOnRight' : -1
                       } #usually jet_pt > 20 (if not verified, use -9999 instead of jet_pt)
'''
'''
variables['djv_ptl2']  = {   'name': '(std_vector_jet_pt[2]>20)*(std_vector_jet_pt[2]/std_vector_lepton_pt[1])+(!(std_vector_jet_pt[2]>20))*(-9999/std_vector_lepton_pt[1])',
                       'range' : (80, 0 ,2), #(10, -1 ,2) (22, -0.21 ,2) 
                       'xaxis' : 'p_{t} jet3 / p_{t}^{lep2}',  
                       'fold' : 1,
                       'SignalOnRight' : -1
                       } #usually jet_pt > 20 (if not verified, use 0 instead of jet_pt)

'''
'''
variables['mjj']  = {  'name': 'mjj',
                      'range': (40,0,2000), #(18,500,2000)(40,0,2000)
                      'xaxis': 'm_{jj} [GeV]',
                      'fold': 3
                      }
'''                      
'''
variables['detajj']  = { 'name': 'detajj',
                         'range': (30,0,9),#(18,2,9)(30,0,9)
			 'xaxis': '#Delta#eta_{jj}',
                         'fold': 3
                       }
'''
'''
variables['ptj3'] = { 'name': 'std_vector_jet_pt[2]',
		      'range': (80, 0., 120.),#(15,0,120)
		      'xaxis': 'p_{t}^{jet 3} [GeV]',
		      'fold': 3,
		      'SignalOnRight' : -1
		      }
''' 
'''
variables['eta1'] = { 'name': 'std_vector_jet_eta[0]',
		      'range': (10, 0., 5.),
		      'xaxis': '#eta^{jet 1}',
		      'fold': 3
		      }


variables['eta2'] = { 'name': 'std_vector_jet_eta[1]',
		      'range': (10, 0., 5.),
		      'xaxis': '#eta^{jet 2}',
		      'fold': 3
		      }
'''

#variables['jv'] = { 'name': '(std_vector_jet_pt[2]<30)',
#		      'range': (4, -1.5, 2.5),
#		      'xaxis': 'jv',
#		      'fold': 3
#		      }

'''
variables['cjv'] = { 'name': '(std_vector_jet_pt[2]<=30 || (std_vector_jet_pt[2]>30 && std_vector_jet_eta[2] < ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[1]) && std_vector_jet_eta[2] > ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[0])))',
		      'range': (4, -1.5, 2.5),
		      'xaxis': 'cjv',
		      'fold': 3
		      }
'''

#variables['etacond']  = {  'name': 'std_vector_jet_eta[2] < ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[1]) && std_vector_jet_eta[2] > ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[0]) ',
                      #'range': (4,-1.5,2.5), 
                      #'xaxis': '#eta condition',
                      #'fold': 3
                      #}
'''
variables['Zlep1'] = { 'name': '(std_vector_lepton_eta[0] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj',
		      'range': (1000, -5., 5.),
		      'xaxis': 'z^{lep 1}',
		      'fold': 3
		      }
'''
'''
variables['Zlep2'] = { 'name': '(std_vector_lepton_eta[1] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj',
		      'range': (10, -5., 5.),
		      'xaxis': 'z^{lep 2}',
		      'fold': 3
		      }
'''
'''
variables['Zjet3'] = { 'name': '(abs((std_vector_jet_eta[2] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj))',
		      'range': (20, 0., 2.),
		      'xaxis': '|z^{jet 3}|',
		      'fold': 3
		      }
		      '''		      
