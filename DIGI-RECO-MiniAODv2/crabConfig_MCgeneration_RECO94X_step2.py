from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'request_RECO94X_INSHORT_DATE'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

# config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_RECO94X_step2.py'
config.JobType.numCores = 4
#config.JobType.maxMemoryMB = 15200
config.JobType.maxMemoryMB = 10000
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = 'DATASETIN'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/cmst3/user/gvonsem/SampleProduction/'
config.Data.publication = True
config.Data.outputDatasetTag = 'DATASETOUT'
config.Data.allowNonValidInputDataset = True

config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T3_US_Baylor']
