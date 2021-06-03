class Generate_Cards_For_Limit():
    
    def __init__(self, **kwargs):
        self.datacard_templete_dic = {}
        self.datacard_templete_dic["2021_5_27"] = "/eos/user/q/qiguo/SWAN_projects/VVV_code/WVV_aQGC/VVV_headfile/limit/AnalyticAnomalousCoupling/templete_card/templete_card.txt"
        
        self.datacard_templete_version = kwargs.get("datacard_templete_version","2021_5_27")
        
        # information in the datacard 
        datacard_information_default = {}
        datacard_information_default["nbins"] = kwargs.get("nbins","4") # number of bins
        datacard_information_default["nnuisance"] = kwargs.get("nnuisance","1") # number of nuisance parameters
        datacard_information_default["channel_name"] = kwargs.get("channel_name", ["ch1","ch2","ch3","ch4"]) # channel name used in the datacard
        datacard_information_default["process_name"] = kwargs.get("process_name", ["sm","quad_cG","sm_lin_quad_cG","BKG"]) # process name used in the datacard  
        datacard_information_default["nprocess_minus_1"] = kwargs.get("nprocess_minus_1", str(len(datacard_information_default["process_name"])-1)) # number of processes minus 1
        self.datacard_information = kwargs.get("datacard_information",datacard_information_default)
        
        self.datacard_content = {}
        
        
    def datacard_content_Channel(self, **kwargs):
        datacard_information = kwargs.get("datacard_information",self.datacard_information)
        datacard_information["channel_name"] = kwargs.get("channel_name", datacard_information["channel_name"])
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        
        datacard_content["channel"] = "".join([i+"    " for i in datacard_information["channel_name"]])
        self.datacard_content["channel"] = "".join([i+"    " for i in datacard_information["channel_name"]])
        
        return datacard_content
    
        
    def datacard_content_observation(self, **kwargs):
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        observation = kwargs.get("observation",["0","0","0","0"]) # observation for each channel
        
        datacard_content["observation"] = "".join([i+"    " for i in observation])
        self.datacard_content["observation"] = "".join([i+"    " for i in observation])
        
        return datacard_content
    
    
    def datacard_content_channel_per_process(self, **kwargs):    
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        datacard_information = kwargs.get("datacard_information",self.datacard_information) 
        channel_name = kwargs.get("channel_name", datacard_information["channel_name"])
        process_name = kwargs.get("process_name", datacard_information["process_name"])
        
        out = "" ; space = "    " # for space between each channel name
        for channel in channel_name:
            for process in process_name:
                out += channel+space
                
        datacard_content["channel_per_process"] = out
        self.datacard_content["channel_per_process"] = out
        
        return datacard_content
    
    
    def datacard_content_process_name_per_channel(self, **kwargs):    
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        datacard_information = kwargs.get("datacard_information",self.datacard_information) 
        channel_name = kwargs.get("channel_name", datacard_information["channel_name"])
        process_name = kwargs.get("process_name", datacard_information["process_name"])
        
        out = "" ; space = "    " # for space between each channel name
        for channel in channel_name:
            for process in process_name:
                out += process+space
                
        datacard_content["process_name_per_channel"] = out
        self.datacard_content["process_name_per_channel"] = out
        
        return datacard_content
    
    
    def datacard_content_process_number_per_channel(self, **kwargs):    
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        datacard_information = kwargs.get("datacard_information",self.datacard_information) 
        channel_name = kwargs.get("channel_name", datacard_information["channel_name"])
        process_name = kwargs.get("process_name", datacard_information["process_name"])
        
        out = "" ; space = "    " # for space between each channel name
        for channel in channel_name:
            for process_number,process in enumerate(process_name):
                out += str(process_number)+space
                
        datacard_content["process_number_per_channel"] = out
        self.datacard_content["process_number_per_channel"] = out
        
        return datacard_content
    
    
    def datacard_content_rate(self, **kwargs):    
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        datacard_information = kwargs.get("datacard_information",self.datacard_information) 
        channel_name = kwargs.get("channel_name", datacard_information["channel_name"])
        process_name = kwargs.get("process_name", datacard_information["process_name"])
        rate = kwargs.get("rate",datacard_content.get("rate",[])) # rate as a dic : like {("ch1","SM"):1}
        
        out = "" ; space = "    " # for space between each channel name
        for channel in channel_name:
            for process_number,process in enumerate(process_name):
                out += rate[(channel,process)]+space
                
        datacard_content["rate"] = out
        self.datacard_content["rate"] = out
        
        return datacard_content
    
    
    def datacard_content_nbins(self, **kwargs):    
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        datacard_information = kwargs.get("datacard_information",self.datacard_information) 
        nbins = kwargs.get("nbins", datacard_information["nbins"])
        
        out = "" ; 
        datacard_content["nbins"] = nbins
        self.datacard_content["nbins"] = nbins
        
        return datacard_content
    
    
    def datacard_content_nprocess_minus_1(self, **kwargs):    
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        datacard_information = kwargs.get("datacard_information",self.datacard_information) 
        nprocess_minus_1 = kwargs.get("nprocess_minus_1", datacard_information["nprocess_minus_1"])
        
        out = "" ; 
        datacard_content["nprocess_minus_1"] = nprocess_minus_1
        self.datacard_content["nprocess_minus_1"] = nprocess_minus_1
        
        return datacard_content
    
    
    def datacard_content_nnuisance(self, **kwargs):    
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        datacard_information = kwargs.get("datacard_information",self.datacard_information) 
        nnuisance = kwargs.get("nnuisance", datacard_information["nnuisance"])
        
        out = "" ; 
        datacard_content["nnuisance"] = nnuisance
        self.datacard_content["nnuisance"] = nnuisance
        
        return datacard_content
    
    
    def datacard_content_Uncertainty(self, **kwargs):    
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        datacard_information = kwargs.get("datacard_information",self.datacard_information) 
        Uncertainty = kwargs.get("Uncertainty", datacard_content.get("Uncertainty",[]))
        channel_name = kwargs.get("channel_name", datacard_information["channel_name"])
        process_name = kwargs.get("process_name", datacard_information["process_name"])
        # Statistics as a dic , like :
        # {"DY_norm":
        # {
        #  "un_type":"lnN",
        #  "un":{("ch1","SM"):1}
        # }
        
        out = "" ; space = "    " # for space between each channel name
        for uncertainty in Uncertainty:
            out += uncertainty+"    "+Uncertainty[uncertainty]['un_type']+"    "
            for channel in channel_name:
                for process_number,process in enumerate(process_name):
                    out += Uncertainty[uncertainty]['un'][(channel,process)]+space
            out += "\n"
        datacard_content["Uncertainty"] = out
        self.datacard_content["Uncertainty"] = out
        
        return datacard_content
    
    
    def datacard_content_f(self, **kwargs):
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        rate = kwargs.get("rate",datacard_content.get("rate",[]))
        Uncertainty = kwargs.get("Uncertainty", datacard_content.get("Uncertainty",[])) 
        
#         rate = kwargs.get("rate1",)
        
        datacard_content = self.datacard_content_nbins( datacard_content = datacard_content )
        datacard_content = self.datacard_content_nprocess_minus_1( datacard_content = datacard_content )
        datacard_content = self.datacard_content_nnuisance( datacard_content = datacard_content )
        datacard_content = self.datacard_content_Channel( datacard_content = datacard_content )
        datacard_content = self.datacard_content_channel_per_process( datacard_content = datacard_content )
        datacard_content = self.datacard_content_observation( datacard_content = datacard_content )
        datacard_content = self.datacard_content_process_name_per_channel( datacard_content = datacard_content )
        datacard_content = self.datacard_content_process_number_per_channel( datacard_content = datacard_content )
        datacard_content = self.datacard_content_rate( datacard_content = datacard_content, rate = rate )
        datacard_content = self.datacard_content_Uncertainty( datacard_content = datacard_content, Uncertainty = Uncertainty )
        
        return datacard_content
        
        
    def Cards(self, **kwargs):
        datacard_in = kwargs.get("datacard_in",self.datacard_templete_dic[self.datacard_templete_version])
        datacard_information = kwargs.get("datacard_information",self.datacard_information)
        datacard_out_name = kwargs.get("datacard_out_name","test.txt")
        datacard_content = kwargs.get("datacard_content",self.datacard_content)
        print_datacard = kwargs.get("print_datacard", False)
        
        f_in = open(datacard_in,"r")
        datacard_in_str = f_in.read()
        
        if print_datacard:
            print(datacard_in_str.format(**datacard_information))
        
        with open(datacard_out_name,"w") as f:
            f.write(datacard_in_str.format(**datacard_content))