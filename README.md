# TrackerRecHitMachineLearning

This repository describes how to read Tracker RecHit information from the ntuples produced with:
https://github.com/cms-legacydata-analyses/TrackerRecHitProducerTool
(need pyROOT and matplotlib installed)

```cd example
xrdcp root://eospublic.cern.ch//eos/opendata/cms/upload/emanuele/step3_QCD600to3000/savehits_output_0001.root .
python3 example.py
```
A scatter plot of the hits from three events should be displayed.
![scatter plot](Figure_1.png?raw=true "Scatter plot")

## Data set content

| Data variable | Type | Description |
| :---------------------- | -----------------: | :---------------------- |
| hit_global_x | `std::vector<float>` | global x position of the RecHit |
| hit_global_y | `std::vector<float>` | global y position of the RecHit |
| hit_global_z | `std::vector<float>` | global z position of the RecHit |
| hit_local_x | `std::vector<float>` | x pos. of the hit in the local sensor coordinate |
| hit_local_y | `std::vector<float>` | y pos. of the hit in the local sensor coordinate |
| hit_local_x_error | `std::vector<float>` | x error in the local sensor coordinate |
| hit_local_y_error | `std::vector<float>` | y error in the local sensor coordinate |
| hit_sub_det | `std::vector<unsigned int>` | subdetector generating the hit [1] |
| hit_layer | `std::vector<unsigned int>` | layer/disk of the subdetector generating the hit |
| hit_type | `std::vector<unsigned int>` | type of sistrip hit [2] |
| hit_simtrack_id | `std::vector<int>` | ID number of the sim track matched to the hit |
| hit_simtrack_index | `std::vector<unsigned int>` | index of the sim track matched to the hit |
| hit_simtrack_match | `std::vector<bool>` | is the hit matched to a sim track? |
| hit_genparticle_id | `std::vector<unsigned int>` | index of the gen particle matched to the hit |
| hit_pdgid | `std::vector<int>` | PDG ID of the gen particle matched to the hit |
| hit_recotrack_id | `std::vector<unsigned int>` | index of the reco track matched to the hit|
| hit_recotrack_match | `std::vector<bool>` | is the hit matched to a reco track? |
| hit_genparticle_match | `std::vector<bool>` | is the hit matched to a gen particle? |
| hit_genjet_id | `std::vector<unsigned int>` | index of the gen jet matched to the hit |
| hit_genjet_match | `std::vector<bool>` | is the hit matched to a gen jet? |
| simtrack_id | `std::vector<unsigned int>` | ID number of the sim track |
| simtrack_pdgid | `std::vector<int>` | PDG ID of the sim track |
| simtrack_charge | `std::vector<int>` | charge of the sim track |
| simtrack_px | `std::vector<float>` | momentum x component of the sim track |
| simtrack_py | `std::vector<float>` | momentum y component of the sim track |
| simtrack_pz | `std::vector<float>` | momentum z component of the sim track |
| simtrack_energy | `std::vector<float>` | energy of the sim track |
| simtrack_vtxid | `std::vector<unsigned int>` | ID number of the sim vertex of the sim track |
| simtrack_genid | `std::vector<unsigned int>` | index of the gen particle associated to the track |
| simtrack_evtid | `std::vector<uint32_t>` | event ID of the sim track |
| genpart_collid | `std::vector<int>` | collision ID of the gen particle |
| genpart_pdgid | `std::vector<int>` | PDG ID of the gen particle |
| genpart_charge | `std::vector<int>` | charge of the gen particle |
| genpart_px | `std::vector<float>` | momentum x component of the gen particle |
| genpart_py | `std::vector<float>` | momentum y component of the gen particle |
| genpart_px | `std::vector<float>` | momentum z component of the gen particle |
| genpart_energy | `std::vector<float>` | energy of the gen particle | 
| genpart_status | `std::vector<int>` | PDG status of the gen particle |
| genjet_px | `std::vector<float>` | momentum x component of the gen jet |
| genjet_py | `std::vector<float>` | momentum y component of the gen jet |
| genjet_pz | `std::vector<float>` | momentum z component of the gen jet |
| genjet_energy | `std::vector<float>` | energy of the gen jet |
| genjet_emEnergy | `std::vector<float>` | electromagnetic energy of the gen jet |
| genjet_hadEnergy | `std::vector<float>` | hadronic energy of the gen jet |
| genjet_invisibleEnergy | `std::vector<float>` | invisible energy of the gen jet |
| genjet_auxiliaryEnergy | `std::vector<float>` | auxiliary energy of the gen jet |
| genjet_const_collid | `std::vector<std::vector<int> >` | collision ID of the constituent of the gen jet |
| genjet_const_pdgid | `std::vector<std::vector<int> >` | PDG ID of the constituent of the gen jet |
| genjet_const_charge | `std::vector<std::vector<int> >` | charge of the constituent of the gen jet |
| genjet_const_px | `std::vector<std::vector<float> >` | momentum x component of the constituent of the gen jet |
| genjet_const_py | `std::vector<std::vector<float> >` | momentum y component of the constituent of the gen jet |
| genjet_const_pz | `std::vector<std::vector<float> >` | momentum z component of the constituent of the gen jet |
| genjet_const_energy | `std::vector<std::vector<float> >` | energy of the constituent of the gen jet |
| track_chi2 | `std::vector<float>` | chi2 of the reco track fit |
| track_ndof | `std::vector<float>` | ndof of the reco track fit |
| track_chi2ndof | `std::vector<float>` | reduced chi2 of the reco track fit |
| track_charge | `std::vector<float>` | charge of the reco track |
| track_momentum | `std::vector<float>` | momentum of the reco track |
| track_pt | `std::vector<float>` | transverse momentum of the reco track |
| track_pterr | `std::vector<float>` | error on the transverse momentum of the reco track |
| track_hitsvalid | `std::vector<unsigned int>`  | number of valid hits in the reco track |
| track_hitslost | `std::vector<unsigned int>`  | number of lost hits in the reco track |
| track_theta | `std::vector<float>` | theta angle of the reco track |
| track_thetaerr | `std::vector<float>` | error on theta of the reco track |
| track_phi | `std::vector<float>` | phi angle of the reco track |
| track_phierr | `std::vector<float>` | error on phi of the reco track |
| track_eta | `std::vector<float>` | pseudorapidity of the reco track |
| track_etaerr | `std::vector<float>` | error on pseudorapidity of the reco track |
| track_dxy | `std::vector<float>` | transverse impact parameter of the reco track |
| track_dxyerr | `std::vector<float>`  | error on the transverse impact parameter of the reco track |
| track_dsz | `std::vector<float>` | longitudinal impact parameter of the reco track |
| track_dszerr | `std::vector<float>` | error on the longitudinal impact parameter of the reco track |
| track_qoverp | `std::vector<float>` | charge over momentum of the reco track |
| track_qoverperr | `std::vector<float>` | error on charge over momentum of the track |
| track_vx | `std::vector<float>` | x position of the vertex of the reco track |
| track_vy | `std::vector<float>` | y position of the vertex of the reco track |
| track_vz | `std::vector<float>` | z position of the vertex of the reco track |
| track_algo | `std::vector<Int_t>` | algorithm type of the reco track |
| track_hit_global_x | `std::vector<std::vector<float> >` | global x position of the RecHit associated to the reco track |
| track_hit_global_y | `std::vector<std::vector<float> >` | global y position of the RecHit associated to the reco track |
| track_hit_global_z | `std::vector<std::vector<float> >` | global z position of the RecHit associated to the reco track |
| track_hit_local_x | `std::vector<std::vector<float> >` | local x position of the RecHit associated to the reco track |
| track_hit_local_y | `std::vector<std::vector<float> >` | local y position of the RecHit associated to the reco track |
| track_hit_local_x_error | `std::vector<std::vector<float> >` | error on local x position of the RecHit associated to the reco track |
| track_hit_local_y_error | `std::vector<std::vector<float> >` | error on local y position of the RecHit associated to the reco track |
| track_hit_sub_det | `std::vector<std::vector<unsigned int> >`  | subdetector generating the hit [1] associated to the reco track |
| track_hit_layer | `std::vector<std::vector<unsigned int> >`  | layer/disk of the subdetector generating the hit associated to the reco track |

[1] 1 PixelBarrel, 2 PixelEndcap, 3 TIB, 4 TID, 5 TOB, 6 TEC

[2] 0 Pixel hit, 1 rphiRecHit, 2 stereoRecHit, 3 rphiRecHitUnmatched, 4 stereoRecHitUnmatched
