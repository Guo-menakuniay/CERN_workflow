# Configure

Use auto_crab help for TTC analysis, have copied to folder $$/scr/PhysicsTools/NanoAODTools/ 

## some configuration files 

```bash
python3 crab_help.py -f input.json -m prepare
```

### crab_help.py

Prepare mode: prepare the crab submit code automatically. Create folders which contain ```*_cfg.py``` codes for crab submiiting.

![image-20221123170313741](/Users/menakuniay/Library/Application Support/typora-user-images/image-20221123170313741.png)

### input.json



### Singal产生

> **Cards path** https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/g2HDM/
>
> **Gridpack path**
>
> ```shell
> /eos/cms/store/group/phys_generator/cvmfs/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/ttc	
> ```
> ref: [marginnote3app://note/20742073-1341-4A68-A994-8C1D0DB55E92](marginnote3app://note/20742073-1341-4A68-A994-8C1D0DB55E92)

gridpack filename:

```
g2HDM_ttc_{X}_M{Y}_rhotu{C1}_rhotc{C2}_rhott00_slc7_amd64_gcc700_CMSSW_ 127 10_6_0_tarball.tar.xz
```

> - {X}: equal A or H ,representing a pseudo-scalar/scalar
> - {Y}: {200,300...,800} representing A/H mass in GeV
> - {C1},{C2}: {00,01,04,10}represecting $\rho_{tu}$, $\rho_{tc}$ coupling values

> Other webs
>
> https://github.com/ExtraYukawa/ttc_bar/blob/lep_mvaID/crab/samples2016_signal.json
>
>  https://github.com/ExtraYukawa/ttc_bar/blob/lep_mvaID/crab/samples2017_signal.json
>
> https://github.com/efeyazgan/exyukawa/tree/master/RandomizedParameters

```
# 查询提交job的状态
crab status -d ./crab_tttZ
```

