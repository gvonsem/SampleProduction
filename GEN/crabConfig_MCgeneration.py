from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'request_DATASET_DATE'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'configs/CONFIG.py'
#config.JobType.numCores = 4
#config.JobType.maxMemoryMB = 
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = 'TTbar_13TeV-sherpa'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = EVENTSJOB
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/cmst3/user/gvonsem/SampleProduction/'
config.Data.publication = True
config.Data.outputDatasetTag = 'DATASET'

config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T3_US_Baylor']
