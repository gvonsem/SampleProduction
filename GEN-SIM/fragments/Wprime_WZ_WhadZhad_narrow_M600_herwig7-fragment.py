import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
 args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/exo_diboson/Spin-1/Wprime_WZ_WhadZhad/narrow/Wprime_WZ_WhadZhad_narrow_M600_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
 nEvents = cms.untracked.uint32(5000),
 numberOfParameters = cms.uint32(1),
 outputFile = cms.string('cmsgrid_final.lhe'),
 scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#Link to datacards:
#https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/exo_diboson/Spin-1/Wprime_WZ_WhadZhad/Wprime_WZ_WhadZhad_narrow_M


#What about the PDF in that block?
from Configuration.Generator.Herwig7Settings.Herwig7LHECommonSettings_cfi import *
#from Configuration.Generator.Herwig7Settings.Herwig7LHEMG5aMCatNLOSettings_cfi.py import *
from Configuration.Generator.Herwig7Settings.Herwig7StableParticlesForDetector_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7CH3TuneSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7PSWeightsSettings_cfi import *


#Inspiration from https://github.com/cms-sw/genproductions/blob/6d430cafd974df5188a4b8c9d33a2747db73e83d/python/ThirteenTeV/Wprime_Hadronizer_TuneEE5C_13TeV_madgraph_differentPDF_herwigpp_cff.py

herwigNewPhysicsBlock = cms.PSet(
    herwigNewPhysics = cms.vstring(
        'cd /Herwig/Particles',
        'create ThePEG::ParticleData wprime',
        'setup wprime 9000002 wprime 600 0.0 0.0 0.0 0 0 3 0',
        'create ThePEG::ParticleData wprimebar',
        'setup wprimebar -9000002 wprimebar 600 0.0 0.0 0.0 0 0 3 0',
        'cd /'
        ),
)

#No change in PDF choice for hard scattering, probably NNLO PDF is used there in MG, https://twiki.cern.ch/twiki/bin/view/CMS/QuickGuideMadGraph5aMCatNLO#PDF_Choice_for_2017_production
#and that PDF is already in herwig7LHECommonSettingsBlock

generator = cms.EDFilter("Herwig7GeneratorFilter",
    herwig7LHECommonSettingsBlock,
    herwigNewPhysicsBlock,
    herwig7StableParticlesForDetectorBlock,
    herwig7CH3SettingsBlock,
    herwig7PSWeightsSettingsBlock,
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(-1),
    dataLocation = cms.string('${HERWIGPATH:-6}'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    filterEfficiency = cms.untracked.double(1.0),
    generatorModule = cms.string('/Herwig/Generators/EventGenerator'),    
    hw_user_settings = cms.vstring(
        'cd /Herwig/EventHandlers',
        'set EventHandler:LuminosityFunction:Energy 13000*GeV',
        'cd /',
        'set /Herwig/Particles/h0:NominalMass 125.0'
    ),    
    parameterSets = cms.vstring(
        'hw_lhe_common_settings',
        'herwigNewPhysics',
        'herwig7CH3PDF', 
        'herwig7CH3AlphaS', 
        'herwig7CH3MPISettings', 
        'herwig7StableParticlesForDetector',
	'hw_PSWeights_settings',
        'hw_user_settings'
    ),
    repository = cms.string('${HERWIGPATH}/HerwigDefaults.rpo'),
    run = cms.string('InterfaceMatchboxTest'),
    runModeList = cms.untracked.string('read,run'),
)
