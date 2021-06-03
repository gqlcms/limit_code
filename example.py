Generate_Cards_For_Limit_ = Generate_Cards_For_Limit()
rate = {}
for i in ["ch1","ch2","ch3","ch4"]:
    for j in ["sm","quad_cG","sm_lin_quad_cG","BKG"]:
        rate[(i,j)] = "dumb_value"
Uncertainty = {"JEC":{"un":{},"un_type":"lnN"}}
for n in ["JEC"]:
    for i in ["ch1","ch2","ch3","ch4"]:
        for j in ["sm","quad_cG","sm_lin_quad_cG","BKG"]:
            Uncertainty["JEC"]["un"][(i,j)] = "1.1"
            
Uncertainty = {'JEC': {'un': {('ch1', 'BKG'): '1.1',
   ('ch1', 'quad_cG'): '1.1',
   ('ch1', 'sm'): '1.1',
   ('ch1', 'sm_lin_quad_cG'): '1.1',
   ('ch2', 'BKG'): '1.1',
   ('ch2', 'quad_cG'): '1.1',
   ('ch2', 'sm'): '1.1',
   ('ch2', 'sm_lin_quad_cG'): '1.1',
   ('ch3', 'BKG'): '1.1',
   ('ch3', 'quad_cG'): '1.1',
   ('ch3', 'sm'): '1.1',
   ('ch3', 'sm_lin_quad_cG'): '1.1',
   ('ch4', 'BKG'): '1.1',
   ('ch4', 'quad_cG'): '1.1',
   ('ch4', 'sm'): '1.1',
   },
  'un_type': 'lnN'}}

datacard_content = Generate_Cards_For_Limit_.datacard_content_f( rate = rate , Uncertainty = Uncertainty)
Generate_Cards_For_Limit_.Cards()
