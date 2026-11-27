# Supplementary Material for BECR-fold Families

## 📰 Citation

**Pham, K., Nicastro, G.G., Long, A.L., et al.** (2026) A structure-guided classification framework reveals the diversity and catalytic architecture of BECR ribonuclease. bioRxiv. [(https://doi.org/10.64898/2026.08.28.747851)](https://doi.org/10.64898/2026.08.28.747851)

---

## 🔎 Contents of This Resource <a id="how-to-use"></a>

Link to download formatted Excel table containing all the sequences at each step of the analysis: [BECR_Sequences.xlsx](https://github.com/KristiPhammie/becr/blob/main/BECR_Sequences.xlsx)

Download .gzipped file of concatenated database: 
- [Download HMM Models (.tar.gz)](https://raw.githubusercontent.com/KristiPhammie/becr/main/hmm.tar.gz) 
- [Download HHM Models (.tar.gz)](https://raw.githubusercontent.com/KristiPhammie/becr/main/hhm.tar.gz) 

<p style="text-align: justify;">This page provides supplemental information for all  BECR-fold proteins identified in our comprehensive classfication study on the BECR superfamily. Each table represents a BECR structural group with a protein family in each row.</p>

- [Colicin-like](https://kristiphammie.github.io/becr/#colicin-like)
- [RNase T2-like](https://kristiphammie.github.io/becr/#rnase-t2-like)
- [EndoU-like](https://kristiphammie.github.io/becr/#endou-like)
- [RNase A-like](https://kristiphammie.github.io/becr/#rnase-a-like)
- [RelE-like](https://kristiphammie.github.io/becr/#rele-like)
- [Barnase-like](https://kristiphammie.github.io/becr/#barnase-like)
- [BECR-like](https://kristiphammie.github.io/becr/#becr-like-like)
- [BECR-Tox2-like](https://kristiphammie.github.io/becr/#becr-tox2-like)

Each table contains the following information for each protein family:

- **Genome Context**: Gene neighborhoods collected with either [Rotifer](https://github.com/leepusp/rotifer.git) or [WebFlaGs](https://server.atkinson-lab.com/webflags)
- **Alignment**: The source of the multiple sequence alignments used to construct a profile HMM used in this study. [PFAM](https://www.ebi.ac.uk/interpro/entry/pfam/#table) (if available), Citation of original publication, or from our work
- **Model**: Downloadable hmm (hmmbuild) and hhm (hhmake) files
- **Molstar**: [Mol*](https://molstar.org/) annotated representative structure

---

## Colicin-like

| Toxin Family | Genome Context | **Alignment** | Model | Annotated Structure (accession) |
| -------------- | ---------------- | ---------------- |--| --------------------------------- |
| <span style="display:inlind-block;width:25px">BECR-Tox1</span> | [Rotifer][BECR-Tox1_gn] | <span style="display:inlind-block;width:100px">[This Resource][BECR-Tox1]</span> | [hmm][BECR-Tox1_hmm] [hhm][BECR-Tox1_hhm] | [A0A417CPW8][BECR-Tox1_molx] |
| BECR-Tox3 | [Rotifer][BECR-Tox3_gn] | [This Resource][BECR-Tox3] | [hmm][BECR-Tox3_hmm] [hhm][BECR-Tox3_hhm] | [A0A3C1G575][BECR-Tox3_molx] |
| BECR-Tox5 | WebFlaGs: [pdf][BECR-Tox5_pdf] [operon.tsv][BECR-Tox5_tsv] [outdesc.txt][BECR-Tox5_txt] | [This Resource][EndoU.2] | [hmm][BECR-Tox5_hmm] [hhm][BECR-Tox5_hhm] | [A0A1V4H847][EndoU.2_molx] |
| Colicin D | [Rotifer][ColicinD_gn] | [PF11429][ColicinD_model] |  | [1V74][ColicinD_molx] |
| Colicin D.2 | [Rotifer][ColicinD.2_gn] | [This Resource][ColicinD.2] |  | [A0A212J498][ColicinD.2_molx] |
| Colicin E5 | [Rotifer][ColicinE5_gn] | [PF12106][ColicinE5_model] |  | [2DFX][ColicinE5_molx] |
| CdiA-CT<sup><sup>Kp342<sup></sup> | [Rotifer][CdiA-CT_Kp342_gn] | [This Resource][CdiA-CT_Kp342] |  | [6CP9][CdiA-CT_Kp342_molx] |
| CdiA-CT<sup>EC3006</sup> | [Rotifer][CdiA-CT_EC3006_gn] | [This Resource][CdiA-CT_EC3006] [Full This Resource][CdiA-CT_EC3006_full] |  | [6CP8][CdiA-CT_EC3006_molx] |
| CdiA-CT<sup>EC869</sup> | [Rotifer][CdiA-CT_EC869_gn] | [This Resource][CdiA-CT_EC869] |  | [7VMC][CdiA-CT_EC869_molx] |
| CdiA-CT<sup>NC101</sup> | [Rotifer][CdiA-CT_NC101_gn] | [This Resource][CdiA-CT_NC101] |  | [5I4Q][CdiA-CT_NC101_molx] |
| CdiA-CT<sup>96.154</sup> | [Rotifer][CdiA-CT_96.154_gn] | [PF14076][CdiA-CT_96.154_pfam] [This Resource][CdiA-CT_96.154_kristi] |  | [D9SFT1][CdiA-CT_96.154_molx] |
| MuF-like | [Rotifer][MuF-like_gn] | [PF18819][MuF-like_pfam] [This Resource][MuF-like_kristi] | [hmm][MuF-like_hmm] [hhm][MuF-like_hhm] | [A0A096XES0][MuF-like_molx] |
| Ntox35 | [Rotifer][Ntox35_gn] | [PF15534][Ntox35] | [hmm][Ntox35_hmm] [hhm][Ntox35_hhm] | [A0A1H3F8X0][Ntox35_molx] |
| Ntox35.2 | [Rotifer][Ntox35.2_gn] | [This Resource][Ntox35.2] | [hmm][Ntox35.2_hmm] [hhm][Ntox35.2_hhm] | [A0A841I6D6][Ntox35.2_molx] |
| PBECR1 | [Rotifer][PBECR1_gn] | [PF18809][PBECR1_model] | [hmm][PBECR1_hmm] [hhm][PBECR1_hhm] | [A0A1F6M7H8][PBECR1_molx] |
| PBECR3 | [Rotifer][PBECR3_gn] | [PF18812][PBECR3_model] | [hmm][PBECR3_hmm] [hhm][PBECR3_hhm] | [A0A0B7GSS4][PBECR3_molx] |
| PBECR3.2 | [Rotifer][PBECR3.2_gn] | [This Resource][PBECR3.2] | [hmm][PBECR3.2_hmm] [hhm][PBECR3.2_hhm] | [A0A4U8UI43][PBECR3.2_molx] |
| PBECR4 | [Rotifer][PBECR4_gn] | [PF18813][PBECR4_model] | [hmm][PBECR4_hmm] [hhm][PBECR4_hhm] | [A0A417QTL2][PBECR4_molx] |
| PBECR4.2 | [Rotifer][PBECR4.2_gn] | [This Resource][PBECR4.2] | [hmm][PBECR4.2_hmm] [hhm][PBECR4.2_hhm] | [A0A2V2DIW2][PBECR4.2_molx] |
| Ntox19 | [Rotifer][Ntox19_gn] | [Nicastro et al., 2026][Ntox19] |  | [A0A5E7QDQ0][Ntox19_molx] |
| Ntox49 | [Rotifer][Ntox49_gn] | [Nicastro et al., 2026][Ntox49] |  | [A0A7H0VXI5][Ntox49_molx] |
| Ntox49.2 | [Rotifer][DUF4258.2_gn] | [This Resource][DUF4258.2] | [hmm][Ntox49.2_hmm] [hhm][Ntox49.2_hhm] | [A0A838VH86][DUF4258.2_molx] |
| Ntox49.3 | WebFlaGs: [pdf][DUF4258.3_pdf] [operon.tsv][DUF4258.3_tsv] [outdesc.txt][DUF4258.3_txt] | [This Resource][DUF4258.3] | [hmm][Ntox49.3_hmm] [hhm][Ntox49.3_hhm] | [A0A1F7XZ82][DUF4258.3_molx] |
| Ntox49.4 | WebFlaGs: [pdf][DUF4258.4_pdf] [operon.tsv][DUF4258.4_tsv] [outdesc.txt][DUF4258.4_txt] | [This Resource][DUF4258.4] | [hmm][Ntox49.4_hmm] [hhm][Ntox49.4_hhm] | [D2UA17][DUF4258.4_molx] |
| Ntox49.5 | [Rotifer][DUF4258.5_gn] | [This Resource][DUF4258.5] | [hmm][Ntox49.5_hmm] [hhm][Ntox49.5_hhm] | [A0A268EH04][DUF4258.5_molx] |

## RNase T2-like

| Toxin Family | Genome Context | Alignment | Model | Annotated Structure (accession) |
| -------------- | ---------------- | ---------------- | - | --------------------------------- |
| RNase T2 | WebFlaGs: [pdf][RNaseT2_pdf] [operon.tsv][RNaseT2_tsv] [outdesc.txt][RNaseT2_txt] | [PF00445][RNaseT2_model] |  | [2EA1][RNaseT2_molx] |

## EndoU-like

| Toxin Family | Genome Context | Alignment | Model | Annotated Structure (accession) |
| -------------- | ---------------- | ---------------- | - | --------------------------------- |
| XendoU | WebFlaGs: [pdf][XendoU_pdf] [operon.tsv][XendoU_tsv] [outdesc.txt][XendoU_txt] | [PF09412][XendoU] | [hmm][XendoU_hmm] [hhm][XendoU_hhm] | [2C1W][XendoU_molx] |
| XendoU.2 | [Rotifer][XendoU.2_gn] | [This Resource][XendoU.2] | [hmm][XendoU.2_hmm] [hhm][XendoU.2_hhm] | [A0A1Z4JKT7][XendoU.2_molx] |
| EndoU | [Rotifer][EndoU_gn] | [PF14436][EndoU] | [hmm][EndoU_hmm] [hhm][EndoU_hhm] | [5HKQ][EndoU_molx] |
| EndoU.3 | WebFlaGs: [pdf][EndoU.3_pdf] [operon.tsv][EndoU.3_tsv] [outdesc.txt][EndoU.3_txt] | [This Resource][EndoU.3] | [hmm][EndoU.3_hmm] [hhm][EndoU.3_hhm] | [A0A1V2YJU1][EndoU.3_molx] |
| EndoU.4 | WebFlaGs: [pdf][EndoU.4_pdf] [operon.tsv][EndoU.4_tsv] [outdesc.txt][EndoU.4_txt] | [This Resource][EndoU.4] | [hmm][EndoU.4_hmm] [hhm][EndoU.4_hhm] | [UPI002E2B26D7][EndoU.4_molx] |
| BC0920 | [Rotifer][BC0920_gn] | [This Resource][BC0920] |  | [Q813X6][BC0920_molx] |
| STox_60 | [Rotifer][STox_60_gn] | [Nicastro et al., 2026][STox_60] | [hmm][STox_60_hmm] [hhm][STox_60_hhm] | [WP_029789863.1][STox_60_molx] |

## RNase A-like

| Toxin Family | Genome Context | Alignment | Model | Annotated Structure (accession) |
| -------------- | ---------------- | ---------------- | - | --------------------------------- |
| RNase A | WebFlaGs: [pdf][RNaseA_pdf] [operon.tsv][RNaseA_tsv] [outdesc.txt][RNaseA_txt] | [PF00074][RNaseA_model] |  | [4WYN][RNaseA_molx] |
| RNase A.2 | WebFlaGs: [pdf][RNaseA.2_pdf] [operon.tsv][RNaseA.2_tsv] [outdesc.txt][RNaseA.2_txt] | [This Resource][RNaseA.2] |  | [A0A3B1IEH8][RNaseA.2_molx] |
| CdiA-CT<sup>Ykris</sup> | [Rotifer][CdiA-CTYkris_gn] | [PF18431][CdiA-CT_Ykris] |  | [5E3E][CdiA-CT_Ykris_molx] |
| Ntox41 | [Rotifer][Ntox41_gn] | [Zhang et al., 2012][Ntox41] | [hmm][Ntox41_hmm] [hhm][Ntox41_hhm] | [A0A0E0USU5][Ntox41_molx] |
| Ntox41.2 | WebFlaGs: [pdf][Ntox41.2_pdf] [operon.tsv][Ntox41.2_tsv] [outdesc.txt][Ntox41.2_txt] | [This Resource][Ntox41.2] | [hmm][Ntox41.2_hmm] [hhm][Ntox41.2_hhm] | [A0A1Q4EYU6][Ntox41.2_molx] |
| Ntox50 | [Rotifer][Ntox50_gn] | [PF15542][Ntox50] | [hmm][Ntox50_hmm] [hhm][Ntox50_hhm] | [A0AAF0CX04][Ntox50_molx] |
| Ntox50.2 | [Rotifer][Ntox50.2_gn] | [This Resource][Ntox50.2] | [hmm][Ntox50.2_hmm] [hhm][Ntox50.2_hhm] | [A0A2G6EE91][Ntox50.2_molx] |


## RelE-like

| Toxin Family | Genome Context | Alignment | Model | Annotated Structure (accession) |
| -------------- | ---------------- | ---------------- | - | --------------------------------- |
| RelE (*Eschericia coli*) | [Rotifer][RelE_E.coli_gn] | [This Resource][RelE_E.coli] |  | [4FXI][RelE_E.coli_molx] |
| RelE (*Methanococcus jannaschii*) | [Rotifer][RelE_M.jannaschii_gn] | [PF06296][RelE_M.jannaschii] |  | [3BPQ][RelE_M.jannaschii_pdb_molx] [A0A917YVE8][RelE_M.jannaschii_afdb_molx] |
| ParE | [Rotifer][ParE_gn] | [PF05016][ParE_pfam] [This Resource][ParE_kristi] | [hmm][ParE_hmm] [hhm][ParE_hhm] | [A0A4V1BZU9][ParE_molx] |
| ParE.2 | [Rotifer][ParE.2_gn] | [This resource][ParE.2] | [hmm][ParE.2_hmm] [hhm][ParE.2_hhm] | [A0A0C1YHU8][ParE.2_molx] |
| ParE.3 | [Rotifer][ParE.3_gn] | [This resource][ParE.3] | [hmm][ParE.3_hmm] [hhm][ParE.3_hhm] | [A0A938YUV1][ParE.3_molx] |
| ParE-like | [Rotifer][ParE-like_gn] | [PF15781][ParE-like_pfam] [This Resource][ParE-like_kristi] | [hmm][ParE-like_hmm] [hhm][ParE-like_hhm] | [A0A0L6U2N9][ParE-like_molx] |
| YoeB | [Rotifer][YoeB_gn] | [PF06769](https://github.com/KristiPhammie/becr/blob/main/html/YoeB.fa) (Raw .fa provided due to file size) [This Resource][YoeB_kristi] | [hmm][YoeB_hmm] [hhm][YoeB_hhm] | [2A6R][YoeB_molx] |
| YafO | [Rotifer][YafO_gn] | [PF13957][YafO] | [hmm][YafO_hmm] [hhm][YafO_hhm] | [A0A3E0TU91][YafO_molx] |
| YhaV | [Rotifer][YhaV_gn] | [PF11663][YhaV_pfam] [This Resource][YhaV_kristi] | [hmm][YhaV_hmm] [hhm][YhaV_hhm] | [A0A1Y2R202][YhaV_molx] |
| HigB | [Rotifer][HigB_gn] | [PF09907][HigB_pfam] [This Resource][HigB_kristi] | [hmm][HigB_hmm] [hhm][HigB_hhm] | [B8F451][HigB_molx] |
| HigB-like | [Rotifer][HigB-like_gn] | [PF05015][HigB-like_pfam] | [hmm][HigB-like_hmm] [hhm][HigB-like_hhm] | [A0A7H0SQA8][HigB-like_molx] |
| BrnT | [Rotifer][BrnT_gn] | [PF04365][BrnT_pfam] [This Resource][BrnT_kristi] | [hmm][BrnT_hmm] [hhm][BrnT_hhm] | [7VD7][BrnT_pdb_molx] [I4B9V8][BrnT_afdb_molx] |
| BrnT.2 | [Rotifer][BrnT.2_gn] | [This Resource][BrnT.2] | [hmm][BrnT.2_hmm] [hhm][BrnT.2_hhm] | [A0A1J5E5S5][BrnT.2_molx] |
| BrnT.3 | [Rotifer][BrnT.3_gn] | [This Resource][BrnT.3] | [hmm][BrnT.3_hmm] [hhm][BrnT.3_hhm] | [A0A8J2XEI7][BrnT.3_molx] |
| MqsR | [Rotifer][MqsR_gn] | [PF15723][MqsR] | [hmm][MqsR_hmm] [hhm][MqsR_hhm] | [3HI2][MqsR_molx] |
| MqsR.2 | [Rotifer][MqsR.2_gn] | [This Resource][MqsR.2] | [hmm][MqsR.2_hmm] [hhm][MqsR.2_hhm] | [A0A9X7T5T6][MqsR.2_molx] |
| MqsR.3 | [Rotifer][MqsR.3_gn] | [This Resource][MqsR.3] | [hmm][MqsR.3_hmm] [hhm][MqsR.3_hhm] | [A0A953XSG8][MqsR.3_molx] |
| YafQ | [Rotifer][YafQ_gn] | [PF15738][YafQ] | [hmm][YafQ_hmm] [hhm][YafQ_hhm] | [4LS4][YafQ_pdb_molx] [L8LVU0][YafQ_afdb_molx] |
| gp49 | WebFlaGs: [pdf][gp49_pdf] [operon.tsv][gp49_tsv] [outdesc.txt][gp49_txt] | [PF05973][gp49_pfam] [This Resource][gp49_kristi] | [hmm][gp49_hmm] [hhm][gp49_hhm] | [7AWK][gp49_pdb_molx] [Q2RNU1][gp49_afdb_molx] |
| RegB | [Rotifer][RegB_gn] | [PF10715][RegB] | [hmm][RegB_hmm] [hhm][RegB_hhm] | [2HX6][RegB_molx] |

## Barnase-like

| Toxin Family | Genome Context | Alignment | Model | Annotated Structure (accession) |
| -------------- | ---------------- | ---------------- | - | --------------------------------- |
| Barnase | [Rotifer][Barnase_gn] | [This Resource][Barnase] | [hmm][Barnase_hmm] [hhm][Barnase_hhm] | [1B20][Barnase_molx] |
| Tox-Ribonuclease | [Rotifer][Tox-Ribonuclease_gn] | [Nicastro et al., 2026][Tox-Ribonuclease] | [hmm][Tox-Ribonuclease_hmm] [hhm][Tox-Ribonuclease_hhm] | [A0A744A5J7][Tox-Ribonuclease_molx] |
| RNase T1 | [Rotifer][RNaseT1_gn] | [This Resource][RNaseT1_model] |  | [1B2M][RNaseT1_molx] |
| RNaseT1.2 | WebFlaGs: [pdf][RNaseT1.2_pdf] [operon.tsv][RNaseT1.2_tsv] [outdescription.txt][RNaseT1.2_txt] | [This Resource][RNaseT1.2] | [hmm][RNaseT1.2_hmm] [hhm][RNaseT1.2_hhm] | [A0A0B1NYA6][RNaseT1.2_molx] |
| RNaseT1.3 | WebFlaGs: [pdf][RNaseT1.3_pdf] [operon.tsv][RNaseT1.3_tsv] [outdescription.txt][RNaseT1.3_txt] | [This Resource][RNaseT1.3] | [hmm][RNaseT1.3_hmm] [hhm][RNaseT1.3_hhm] | [A0A9W9CSS5][RNaseT1.3_molx] |
| Sarcin | [Rotifer][Sarcin_gn] | [This Resource][Sarcin_model] [Full This Resource][Sarcin_full_model] | [hmm][Sarcin_hmm] [hhm][Sarcin_hhm] | [1DE3][Sarcin_molx] |

## BECR-like

| Toxin Family | Genome Context | Alignment | Model | Annotated Structure (accession) |
| -------------- | ---------------- | ---------------- | - | --------------------------------- |
| BECR-like-Tox1 | [Rotifer][EndoVII_gn] | [PF15657][EndoVII_pfam] [This Resource][EndoVII_kristi] |  | [U2R0G2][PF15657_molx] |
| BECR-like-Tox1.2 | [Rotifer][EndoVII.2_gn] | [This Resource][EndoVII.2] | [hmm][BECR-like-Tox1.2_hmm] [hhm][BECR-like-Tox1.2_hhm] | [A0A1N7BT64][EndoVII.2_molx] |
| Ntox7 | [Rotifer][Ntox7_gn] | [Nicastro et al., 2026][Ntox7] |  | [A0A5J5FSA8][Ntox7_molx] |
| Ntox7.2 | [Rotifer][Ntox7.2_gn] | [This Resource][Ntox7.2] | [hmm][Ntox7.2_hmm] [hhm][Ntox7.2_hhm] | [A0A369YFT7][Ntox7.2_molx] |
| Ntox7.3 | WebFlaGs: [pdf][Ntox7.3_pdf] [operon.tsv][Ntox7.3_tsv] [outdesc.txt][Ntox7.3_txt] | [This Resource][Ntox7.3] | [hmm][Ntox7.3_hmm] [hhm][Ntox7.3_hhm] | [A0A7Y4YHE2][Ntox7.3_molx] |
| Ntox36 | [Rotifer][Ntox36_gn] | [Zhang et al., 2012][Ntox36_zhang] [This Resource][Ntox36] | [hmm][Ntox36_hmm] [hhm][Ntox36_hhm] | [Q7NP45][Ntox36_molx] |
| Ntox47.st1 | [Rotifer][Ntox47.st1_gn] | [Nicastro et al., 2026][Ntox47.st1.gian] [This Resource][Ntox47.st1.kristi] | [hmm][Ntox47.st1_hmm] [hhm][Ntox47.st1_hhm] | [A0A740SFH9][Ntox47.st1_molx] |
| Ntox47.st2 | [Rotifer][Ntox47.st2_gn] | [Nicastro et al., 2026][Ntox47.st2.gian] | [hmm][Ntox47.st2_hmm] [hhm][Ntox47.st2_hhm] | [A0A747XMS3][Ntox47.st2_molx] |
| Stox_2 | [Rotifer][STox_2_gn] | [Nicastro et al., 2026][Stox_2] |  | [WP_212722943.1][Stox_2_molx] |
| STox_6 | [Rotifer][STox_6_gn] | [Nicastro et al., 2026][STox_6] | [hmm][STox_6_hmm] [hhm][STox_6_hhm] | [A0A748UZW8][STox_6_molx] |
| STox_11 | [Rotifer][STox_11_gn] | [Nicastro et al., 2026][STox_11] [This Resource][STox_11_kristi] | [hmm][STox_11_hmm] [hhm][STox_11_hhm] | [A0A4V1G7W5][STox_11_molx] |
| STox_11.2 | [Rotifer][STox_11.2_gn] | [This Resource][STox_11.2] | [hmm][STox_11.2_hmm] [hhm][STox_11.2_hhm] | [A0A7X0PHU6][STox_11.2_molx] |
| STox_11.3 | [Rotifer][STox_11.3_gn] | [This Resource][STox_11.3] | [hmm][STox_11.3_hmm] [hhm][STox_11.3_hhm] | [A0A939KTB7][STox_11.3_molx] |
| STox_32 | [Rotifer][STox_32_gn] | [This Resource][STox_32_kristi] | [hmm][STox_32_hmm] [hhm][STox_32_hhm] | [UPI00217D55C6][STox_32_molx] |
| STox_37 | [Rotifer][STox_37_gn] | [Nicastro et al., 2026][STox_37_gian] [This Resource][STox_37] | [hmm][STox_37_hmm] [hhm][STox_37_hhm] | [A0A1M6MZG2][STox_37_molx] |
| STox_39 | [Rotifer][STox_39_gn] | [Nicastro et al., 2026][STox_39] [This Resource][STox_39_kristi] | [hmm][STox_39_hmm] [hhm][STox_39_hhm] | [A0A5T2NHZ2][STox_39_molx] |
| STox_39.2 | [Rotifer][STox_39.2_gn] | [This Resource][STox_39.2] | [hmm][STox_39.2_hmm] [hhm][STox_39.2_hhm] | [A0A937AZC2][STox_39.2_molx] |
| STox_57 | [Rotifer][STox_57_gn] | [Nicastro et al., 2026][STox_57] | [hmm][STox_57_hmm] [hhm][STox_57_hhm] | [A0A3S4HEL1][STox_57_molx] |
| STox_58 | [Rotifer][STox_58_gn] | [Nicastro et al., 2026][STox_58] | [hmm][STox_58_hmm] [hhm][STox_58_hhm] | [A0A5X8N7M2][STox_58_molx] |
| STox_59 | [Rotifer][STox_59_gn] | [Nicastro et al., 2026][STox_59] | [hmm][STox_59_hmm] [hhm][STox_59_hhm] | [A0A6X8NAU9][STox_59_molx] |
| YeeF | [Rotifer][YeeF_gn] | [This resource][YeeF_model] | [hmm][YeeF_hmm] [hhm][YeeF_hhm] | [O31506][YeeF_molx] |
| STox_1 | [Rotifer][STox_1_gn] | [Nicastro et al., 2026][STox_1] | [hmm][STox_1_hmm] [hhm][STox_1_hhm] | [FD01543133_03431][STox_1_molx] |
| STox_3 | [Rotifer][STox_3_gn] | [Nicastro et al., 2026][STox_3] | [hmm][STox_3_hmm] [hhm][STox_3_hhm] | [A0A3Z2V253][STox_3_molx] |
| STox_4 | [Rotifer][STox_4_gn] | [Nicastro et al., 2026][STox_4] | [hmm][STox_4_hmm] [hhm][STox_4_hhm] | [A0A3Y4H1N0][STox_4_molx] |
| STox_4.2 | [Rotifer][STox_4.2_gn] | [This Resource][STox_4.2] | [hmm][STox_4.2_hmm] [hhm][STox_4.2_hhm] | [A0A7V8VAQ0][STox_4.2_molx] |
| STox_55 | [Rotifer][STox_55_gn] | [Nicastro et al., 2026][STox_55] | [hmm][STox_55_hmm] [hhm][STox_55_hhm] | [WP_117405990.1][STox_55_molx] |

## BECR-Tox2-like

| Toxin Family | Genome Context | Alignment | Model | Annotated Structure (accession) |
| -------------- | ---------------- | ---------------- | - | --------------------------------- |
| BECR-Tox2 | [Rotifer][BECR-Tox2_gn] WebFlaGs: [pdf][BECR-Tox2_pdf] [operon.tsv][BECR-Tox2_tsv] [outdescription.txt][BECR-Tox2.txt] | [This Resource][BECR-Tox2] | [hmm][BECR-Tox2_hmm] [hhm][BECR-Tox2_hhm] | [A0A352X7W3][BECR-Tox2_molx] |
| CdiA-CT<sup>ECL</sup> | [Rotifer][CdiA-CT_ECL_gn] | [PF14426][CdiA-CT_ECL_pfam] [This Resource][CdiA-CT_ECL_kristi] |  | [4NTQ][CdiA-CT_ECL_molx] |
| Ntox18.st1 | [Rotifer][Ntox18.st1_gn] | [Nicastro et al., 2026][Ntox18.st1] | [hmm][Ntox18.st1_hmm] [hhm][Ntox18.st1_hhm] | [A0A3Y4H1N0][Ntox18.st1_molx] |
| Ntox18.st2 | [Rotifer][Ntox18.st2_gn] | [Nicastro et al., 2026][Ntox18.st2] | [hmm][Ntox18.st2_hmm] [hhm][Ntox18.st2_hhm] | [A0A7T8FFU2][Ntox18.st2_molx] |

## Undetermined

| Toxin Family | Genome Context | Alignment | Model | Annotated Structure (accession) |
| -------------- | ---------------- | ---------------- |  | --------------------------------- |
| BECR-Tox4 | WebFlaGs: [pdf][BECR-Tox4_pdf] [operon.tsv][BECR-Tox4_tsv] [outdescription.txt][BECR-Tox4.txt] | [This Resource][BECR-Tox4] | [hmm][BECR-Tox4_hmm] [hhm][BECR-Tox4_hhm] | [A0A1F9Y1D8][BECR-Tox4_molx] |
| PBECR5 | [Rotifer][PBECR5_gn] | [PF18814][PBECR5_model] | [hmm][PBECR5_hmm] [hhm][PBECR5_hhm] | [A0A396QF16][PBECR5_molx] |

<!-- Genome context PDFs -->
[BECR-Tox1_gn]: https://KristiPhammie.github.io/becr/pdf/BECR-Tox1.pdf
[BECR-Tox3_gn]: https://KristiPhammie.github.io/becr/pdf/BECR-Tox3.pdf
[BECR-Tox5_pdf]: https://KristiPhammie.github.io/becr/webflags/BECR-Tox5/results_TreeOrder_output.pdf
[BECR-Tox5_tsv]: https://KristiPhammie.github.io/becr/webflags/BECR-Tox5/results_TreeOrder_operon.tsv
[BECR-Tox5_txt]: https://KristiPhammie.github.io/becr/webflags/BECR-Tox5/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[ColicinD_gn]: https://KristiPhammie.github.io/becr/pdf/ColicinD.pdf
[ColicinD.2_gn]: https://KristiPhammie.github.io/becr/pdf/ColicinD.2.pdf
[ColicinE5_gn]: https://KristiPhammie.github.io/becr/pdf/ColicinE5.pdf
[CdiA-CT_Kp342_gn]: https://KristiPhammie.github.io/becr/pdf/CdiA-CT_Kp342.pdf
[CdiA-CT_ECL_gn]: https://KristiPhammie.github.io/becr/pdf/CdiA-CT_ECL.pdf
[CdiA-CT_EC3006_gn]: https://KristiPhammie.github.io/becr/pdf/CdiA-CT_EC3006.pdf
[CdiA-CT_EC869_gn]: https://KristiPhammie.github.io/becr/pdf/CdiA-CT_EC869.pdf
[CdiA-CT_NC101_gn]: https://KristiPhammie.github.io/becr/pdf/CdiA-CT_NC101.pdf
[CdiA-CT_96.154_gn]: https://KristiPhammie.github.io/becr/pdf/CdiA-CT_96.154.pdf
[DUF4258.2_gn]: https://KristiPhammie.github.io/becr/pdf/DUF4258.2.pdf
[DUF4258.3_pdf]: https://KristiPhammie.github.io/becr/webflags/DUF4258.3/results_TreeOrder_output.pdf
[DUF4258.3_tsv]: https://KristiPhammie.github.io/becr/webflags/DUF4258.3/results_TreeOrder_operon.tsv
[DUF4258.3.txt]: https://KristiPhammie.github.io/becr/webflags/DUF4258.3/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[DUF4258.4_pdf]: https://KristiPhammie.github.io/becr/webflags/DUF4258.4/results_TreeOrder_output.pdf
[DUF4258.4_tsv]: https://KristiPhammie.github.io/becr/webflags/DUF4258.4/results_TreeOrder_operon.tsv
[DUF4258.4_txt]: https://KristiPhammie.github.io/becr/webflags/DUF4258.4/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[DUF4258.5_gn]: https://KristiPhammie.github.io/becr/pdf/DUF4258.5.pdf
[RNaseT2_pdf]: https://KristiPhammie.github.io/becr/webflags/RNaseT2/results_TreeOrder_output.pdf
[RNaseT2_tsv]: https://KristiPhammie.github.io/becr/webflags/RNaseT2/results_TreeOrder_operon.tsv
[RNaseT2_txt]: https://KristiPhammie.github.io/becr/webflags/RNaseT2/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[MuF-like_gn]: https://KristiPhammie.github.io/becr/pdf/MuF-like.pdf
[Ntox35_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox35.pdf
[Ntox35.2_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox35.2.pdf
[PBECR1_gn]: https://KristiPhammie.github.io/becr/pdf/PBECR1.pdf
[PBECR3_gn]: https://KristiPhammie.github.io/becr/pdf/PBECR3.pdf
[PBECR3.2_gn]: https://KristiPhammie.github.io/becr/pdf/PBECR3.2.pdf
[PBECR4_gn]: https://KristiPhammie.github.io/becr/pdf/PBECR4.pdf
[PBECR4.2_gn]: https://KristiPhammie.github.io/becr/pdf/PBECR4.2.pdf
[Ntox19_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox19.st.pdf
[Ntox49_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox49_1.pdf

[RelE_E.coli_gn]: https://KristiPhammie.github.io/becr/pdf/RelE_E.coli.pdf
[RelE_M.jannaschii_gn]: https://KristiPhammie.github.io/becr/pdf/RelE_M.jannaschii.pdf
[ParE_gn]: https://KristiPhammie.github.io/becr/pdf/ParE.pdf
[ParE.2_gn]: https://KristiPhammie.github.io/becr/pdf/ParE.2.pdf
[ParE.3_gn]: https://KristiPhammie.github.io/becr/pdf/ParE.3.pdf
[ParE-like_gn]: https://KristiPhammie.github.io/becr/pdf/ParE-like.pdf
[YoeB_gn]: https://KristiPhammie.github.io/becr/pdf/YoeB.pdf
[YafO_gn]: https://KristiPhammie.github.io/becr/pdf/YafO.pdf
[YhaV_gn]: https://KristiPhammie.github.io/becr/pdf/YhaV.pdf
[HigB_gn]: https://KristiPhammie.github.io/becr/pdf/HigB.pdf
[HigB-like_gn]: https://KristiPhammie.github.io/becr/pdf/HigB-like.pdf
[BrnT_gn]: https://KristiPhammie.github.io/becr/pdf/BrnT.pdf
[BrnT.2_gn]: https://KristiPhammie.github.io/becr/pdf/BrnT.2.pdf
[BrnT.3_gn]: https://KristiPhammie.github.io/becr/pdf/BrnT.3.pdf
[MqsR_gn]: https://KristiPhammie.github.io/becr/pdf/MqsR.pdf
[MqsR.2_gn]: https://KristiPhammie.github.io/becr/pdf/MqsR.2.pdf
[MqsR.3_gn]: https://KristiPhammie.github.io/becr/pdf/MqsR.3.pdf
[YafQ_gn]: https://KristiPhammie.github.io/becr/pdf/YafQ.pdf
[gp49_pdf]: https://KristiPhammie.github.io/becr/webflags/gp49/results_TreeOrder_output.pdf
[gp49_tsv]: https://KristiPhammie.github.io/becr/webflags/gp49/results_TreeOrder_operon.tsv
[gp49_txt]: https://KristiPhammie.github.io/becr/webflags/gp49/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[RegB_gn]: https://KristiPhammie.github.io/becr/pdf/RegB.pdf

[XendoU_pdf]: https://KristiPhammie.github.io/becr/webflags/XendoU/results_TreeOrder_output.pdf
[XendoU_tsv]: https://KristiPhammie.github.io/becr/webflags/XendoU/results_TreeOrder_operon.tsv
[XendoU_txt]: https://KristiPhammie.github.io/becr/webflags/XendoU/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[XendoU.2_gn]: https://KristiPhammie.github.io/becr/pdf/XendoU.2.pdf
[EndoU_gn]: https://KristiPhammie.github.io/becr/pdf/EndoU.pdf
[EndoU.3_pdf]: https://KristiPhammie.github.io/becr/webflags/EndoU.3/results_TreeOrder_output.pdf
[EndoU.3_tsv]: https://KristiPhammie.github.io/becr/webflags/EndoU.3/results_TreeOrder_operon.tsv
[EndoU.3_txt]: https://KristiPhammie.github.io/becr/webflags/EndoU.3/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[EndoU.4_pdf]: https://KristiPhammie.github.io/becr/webflags/EndoU.4/results_TreeOrder_output.pdf
[EndoU.4_tsv]: https://KristiPhammie.github.io/becr/webflags/EndoU.4/results_TreeOrder_operon.tsv
[EndoU.4_txt]: https://KristiPhammie.github.io/becr/webflags/EndoU.4/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[DUF4258.3_pdf]: https://KristiPhammie.github.io/becr/webflags/DUF4258.3/results_TreeOrder_output.pdf
[DUF4258.3_tsv]: https://KristiPhammie.github.io/becr/webflags/DUF4258.3/results_TreeOrder_operon.tsv
[DUF4258.3_txt]: https://KristiPhammie.github.io/becr/webflags/DUF4258.3/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[BC0920_gn]: https://KristiPhammie.github.io/becr/pdf/BC0920.pdf
[STox_60_gn]: https://KristiPhammie.github.io/becr/pdf/STox_60.pdf

[RNaseA_pdf]: https://KristiPhammie.github.io/becr/webflags/RNaseA/results_TreeOrder_output.pdf
[RNaseA_tsv]: https://KristiPhammie.github.io/becr/webflags/RNaseA/results_TreeOrder_operon.tsv
[RNaseA_txt]: https://KristiPhammie.github.io/becr/webflags/RNaseA/results_flankgene.fasta_cluster_out_1_1e-10_outdesc.txt
[RNaseA.2_pdf]: https://KristiPhammie.github.io/becr/webflags/RNaseA.2/results_TreeOrder_output.pdf
[RNaseA.2_tsv]: https://KristiPhammie.github.io/becr/webflags/RNaseA.2/results_TreeOrder_operon.tsv
[RNaseA.2_txt]: https://KristiPhammie.github.io/becr/webflags/RNaseA.2/results_flankgene.fasta_cluster_out_1_1e-10_outdesc.txt
[CdiA-CTYkris_gn]: https://KristiPhammie.github.io/becr/pdf/CdiA-CT_Ykris.pdf
[Ntox41_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox41.pdf
[Ntox41.2_pdf]: https://KristiPhammie.github.io/becr/webflags/Ntox41.2/results_TreeOrder_output.pdf
[Ntox41.2_tsv]: https://KristiPhammie.github.io/becr/webflags/Ntox41.2/results_TreeOrder_operon.tsv
[Ntox41.2_txt]: https://KristiPhammie.github.io/becr/webflags/Ntox41.2/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[Ntox50_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox50.pdf
[Ntox50.2_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox50.2.pdf

[EndoVII_gn]: https://KristiPhammie.github.io/becr/pdf/EndoVII.pdf
[EndoVII.2_gn]: https://KristiPhammie.github.io/becr/pdf/EndoVII.2.pdf
[Ntox7_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox7.pdf
[Ntox7.2_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox7.2.pdf
[Ntox7.3_pdf]: https://KristiPhammie.github.io/becr/webflags/Ntox7.3/results_TreeOrder_output.pdf
[Ntox7.3_tsv]: https://KristiPhammie.github.io/becr/webflags/Ntox7.3/results_TreeOrder_operon.tsv
[Ntox7.3_txt]: https://KristiPhammie.github.io/becr/webflags/Ntox7.3/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[Ntox36_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox36.pdf
[Ntox47.st1_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox47.st1.pdf
[Ntox47.st2_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox47.st2.pdf
[STox_2_gn]: https://KristiPhammie.github.io/becr/pdf/STox_2.pdf
[STox_6_gn]: https://KristiPhammie.github.io/becr/pdf/STox_6.pdf
[STox_11_gn]: https://KristiPhammie.github.io/becr/pdf/STox_11.pdf
[STox_11.2_gn]: https://KristiPhammie.github.io/becr/pdf/STox_11.2.pdf
[STox_11.3_gn]: https://KristiPhammie.github.io/becr/pdf/STox_11.3.pdf
[STox_32_gn]: https://KristiPhammie.github.io/becr/pdf/STox_32.pdf
[STox_39_gn]: https://KristiPhammie.github.io/becr/pdf/STox_39.pdf
[STox_39.2_gn]: https://KristiPhammie.github.io/becr/pdf/STox_39.2.pdf
[STox_57_gn]: https://KristiPhammie.github.io/becr/pdf/STox_57.pdf
[STox_58_gn]: https://KristiPhammie.github.io/becr/pdf/STox_58.pdf
[STox_59_gn]: https://KristiPhammie.github.io/becr/pdf/STox_59.pdf
[YeeF_gn]: https://KristiPhammie.github.io/becr/pdf/YeeF.pdf

[Barnase_gn]: https://KristiPhammie.github.io/becr/pdf/Barnase.pdf
[Tox-Ribonuclease_gn]: https://KristiPhammie.github.io/becr/pdf/Tox-Ribonuclease.pdf

[STox_1_gn]: https://KristiPhammie.github.io/becr/pdf/STox_1.pdf
[STox_3_gn]: https://KristiPhammie.github.io/becr/pdf/STox_3.pdf
[STox_4_gn]: https://KristiPhammie.github.io/becr/pdf/STox_4.pdf
[STox_4.2_gn]: https://KristiPhammie.github.io/becr/pdf/STox_4.2.pdf
[STox_55_gn]: https://KristiPhammie.github.io/becr/pdf/STox_55.pdf

[BECR-Tox2_gn]: https://KristiPhammie.github.io/becr/pdf/BECR-Tox2.pdf
[BECR-Tox2_pdf]: https://KristiPhammie.github.io/becr/webflags/BECR-Tox2/results_TreeOrder_output.pdf
[BECR-Tox2_tsv]: https://KristiPhammie.github.io/becr/webflags/BECR-Tox2/results_TreeOrder_operon.tsv
[BECR-Tox2.txt]: https://KristiPhammie.github.io/becr/webflags/BECR-Tox2/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[STox_37_gn]: https://KristiPhammie.github.io/becr/pdf/STox_37.pdf
[PBECR5_gn]: https://KristiPhammie.github.io/becr/pdf/PBECR5.pdf
[Ntox48_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox48.pdf
[CdiA-CTECL_gn]: https://KristiPhammie.github.io/becr/pdf/CdiA-CT_ECL.pdf
[Ntox18.st1_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox18.st1.pdf
[Ntox18.st2_gn]: https://KristiPhammie.github.io/becr/pdf/Ntox18.st2.pdf
[RNaseT1_gn]: https://KristiPhammie.github.io/becr/pdf/RNaseT1.pdf
[RNaseT1.2_pdf]: https://KristiPhammie.github.io/becr/webflags/RNaseT1.2/results_TreeOrder_output.pdf
[RNaseT1.2_tsv]: https://KristiPhammie.github.io/becr/webflags/RNaseT1.2/results_TreeOrder_operon.tsv
[RNaseT1.2_txt]: https://KristiPhammie.github.io/becr/webflags/RNaseT1.2/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[RNaseT1.3_pdf]: https://KristiPhammie.github.io/becr/webflags/RNaseT1.3/results_TreeOrder_output.pdf
[RNaseT1.3_tsv]: https://KristiPhammie.github.io/becr/webflags/RNaseT1.3/results_TreeOrder_operon.tsv
[RNaseT1.3_txt]: https://KristiPhammie.github.io/becr/webflags/RNaseT1.3/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt
[Sarcin_gn]: https://KristiPhammie.github.io/becr/pdf/Sarcin.pdf

[BECR-Tox4_pdf]: https://KristiPhammie.github.io/becr/webflags/BECR-Tox4/results_TreeOrder_output.pdf
[BECR-Tox4_tsv]: https://KristiPhammie.github.io/becr/webflags/BECR-Tox4/results_TreeOrder_operon.tsv
[BECR-Tox4.txt]: https://KristiPhammie.github.io/becr/webflags/BECR-Tox4/results_flankgene.fasta_cluster_out_1_1e-05_outdesc.txt

<!-- HTML models -->
[BECR-Tox1]: https://KristiPhammie.github.io/becr/html/BECR-Tox1.html
[BECR-Tox3]: https://KristiPhammie.github.io/becr/html/BECR-Tox3.html
[BECR-Tox4]: https://KristiPhammie.github.io/becr/html/BECR-Tox4.html
[ColicinD_model]: https://KristiPhammie.github.io/becr/html/ColicinD.html
[ColicinD.2]: https://KristiPhammie.github.io/becr/html/ColicinD.2.html
[ColicinE5_model]: https://KristiPhammie.github.io/becr/html/ColicinE5.html
[CdiA-CT_Kp342]: https://KristiPhammie.github.io/becr/html/CdiA-CT_Kp342.html
[CdiA-CT_EC3006]: https://KristiPhammie.github.io/becr/html/CdiA-CT_EC3006.html
[CdiA-CT_EC3006_full]: https://KristiPhammie.github.io/becr/html/CdiA-CT_EC3006_full.html
[CdiA-CT_EC869]: https://KristiPhammie.github.io/becr/html/CdiA-CT_EC869.html
[CdiA-CT_NC101]: https://KristiPhammie.github.io/becr/html/CdiA-CT_NC101.html
[CdiA-CT_96.154_pfam]: https://KristiPhammie.github.io/becr/html/CdiA-CT_96.154_pfam.html
[CdiA-CT_96.154_kristi]: https://KristiPhammie.github.io/becr/html/CdiA-CT_96.154_kristi.html
[DUF4258.2]: https://KristiPhammie.github.io/becr/html/DUF4258.2.html
[DUF4258.3]: https://KristiPhammie.github.io/becr/html/DUF4258.3.html
[DUF4258.4]: https://KristiPhammie.github.io/becr/html/DUF4258.4.html
[DUF4258.5]: https://KristiPhammie.github.io/becr/html/DUF4258.5.html
[RNaseT2_model]: https://KristiPhammie.github.io/becr/html/RNaseT2.html
[MuF-like_pfam]: https://KristiPhammie.github.io/becr/html/MuF-like_pfam.html
[MuF-like_kristi]: https://KristiPhammie.github.io/becr/html/MuF-like_kristi.html
[Ntox35]: https://KristiPhammie.github.io/becr/html/Ntox35.html
[Ntox35.2]: https://KristiPhammie.github.io/becr/html/Ntox35.2.html
[PBECR1_model]: https://KristiPhammie.github.io/becr/html/PBECR1.html
[PBECR3_model]: https://KristiPhammie.github.io/becr/html/PBECR3.html
[PBECR3.2]: https://KristiPhammie.github.io/becr/html/PBECR3.2.html
[PBECR4_model]: https://KristiPhammie.github.io/becr/html/PBECR4.html
[PBECR4.2]: https://KristiPhammie.github.io/becr/html/PBECR4.2.html
[Ntox19]: https://KristiPhammie.github.io/becr/html/Ntox19.st.html
[Ntox49]: https://KristiPhammie.github.io/becr/html/Ntox49.st.html
[RelE_E.coli]: https://KristiPhammie.github.io/becr/html/RelE_E.coli.html
[RelE_M.jannaschii]: https://KristiPhammie.github.io/becr/html/RelE_M.jannaschii.html
[ParE_pfam]: https://KristiPhammie.github.io/becr/html/ParE_pfam.html
[ParE_kristi]: https://KristiPhammie.github.io/becr/html/ParE_kristi.html
[ParE.2]: https://KristiPhammie.github.io/becr/html/ParE.2.html
[ParE.3]: https://KristiPhammie.github.io/becr/html/ParE.3.html
[ParE-like_pfam]: https://KristiPhammie.github.io/becr/html/ParE-like_pfam.html
[ParE-like_kristi]: https://KristiPhammie.github.io/becr/html/ParE-like_kristi.html
[YoeB_pfam]: https://KristiPhammie.github.io/becr/html/YoeB_pfam.html
[YoeB_kristi]: https://KristiPhammie.github.io/becr/html/YoeB_kristi.html
[YafO]: https://KristiPhammie.github.io/becr/html/YafO.html
[YhaV_pfam]: https://KristiPhammie.github.io/becr/html/YhaV_pfam.html
[YhaV_kristi]: https://KristiPhammie.github.io/becr/html/YhaV_kristi.html
[HigB_pfam]: https://KristiPhammie.github.io/becr/html/HigB_pfam.html
[HigB_kristi]: https://KristiPhammie.github.io/becr/html/HigB_kristi.html
[HigB-like_pfam]: https://KristiPhammie.github.io/becr/html/HigB-like_pfam.html
[BrnT_pfam]: https://KristiPhammie.github.io/becr/html/BrnT_pfam.html
[BrnT_kristi]: https://KristiPhammie.github.io/becr/html/BrnT_kristi.html
[BrnT.2]: https://KristiPhammie.github.io/becr/html/BrnT.2.html
[BrnT.3]: https://KristiPhammie.github.io/becr/html/BrnT.3.html
[MqsR]: https://KristiPhammie.github.io/becr/html/MqsR_pfam.html
[MqsR.2]: https://KristiPhammie.github.io/becr/html/MqsR.2.html
[MqsR.3]: https://KristiPhammie.github.io/becr/html/MqsR.3.html
[YafQ]: https://KristiPhammie.github.io/becr/html/YafQ_pfam.html
[gp49_pfam]: https://KristiPhammie.github.io/becr/html/gp49_pfam.html
[gp49_kristi]: https://KristiPhammie.github.io/becr/html/gp49_kristi.html
[RegB]: https://KristiPhammie.github.io/becr/html/RegB.html
[XendoU]: https://KristiPhammie.github.io/becr/html/XendoU.html
[XendoU.2]: https://KristiPhammie.github.io/becr/html/XendoU.2.html
[EndoU]: https://KristiPhammie.github.io/becr/html/EndoU.html
[EndoU.2]: https://KristiPhammie.github.io/becr/html/BECR-Tox5.html
[EndoU.3]: https://KristiPhammie.github.io/becr/html/EndoU.3.html
[EndoU.4]: https://KristiPhammie.github.io/becr/html/EndoU.4.html
[BC0920]: https://KristiPhammie.github.io/becr/html/BC0920.html
[STox_60]: https://KristiPhammie.github.io/becr/html/STox_60.html
[RNaseA_model]: https://KristiPhammie.github.io/becr/html/RNaseA.html
[RNaseA.2]: https://KristiPhammie.github.io/becr/html/RNaseA.2.html
[CdiA-CT_Ykris]: https://KristiPhammie.github.io/becr/html/CdiA-CT_Ykris.html
[Ntox41]: https://KristiPhammie.github.io/becr/html/Ntox41.html
[Ntox41.2]: https://KristiPhammie.github.io/becr/html/Ntox41.2.html
[Ntox50]: https://KristiPhammie.github.io/becr/html/Ntox50.html
[Ntox50.2]: https://KristiPhammie.github.io/becr/html/Ntox50.2.html
[EndoVII_pfam]: https://KristiPhammie.github.io/becr/html/EndoVII_pfam.html
[EndoVII_kristi]: https://KristiPhammie.github.io/becr/html/EndoVII_kristi.html
[EndoVII.2]: https://KristiPhammie.github.io/becr/html/EndoVII.2.html
[Ntox7]: https://KristiPhammie.github.io/becr/html/Ntox7.html
[Ntox7.2]: https://KristiPhammie.github.io/becr/html/Ntox7.2.html
[Ntox7.3]: https://KristiPhammie.github.io/becr/html/Ntox7.3.html
[Ntox36_zhang]: https://KristiPhammie.github.io/becr/html/Ntox36_zhang.html
[Ntox36]: https://KristiPhammie.github.io/becr/html/Ntox36_kristi.html
[Ntox47.st1.gian]: https://KristiPhammie.github.io/becr/html/Ntox47.st1.gian.html
[Ntox47.st1.kristi]: https://KristiPhammie.github.io/becr/html/Ntox47.st1.kristi.html
[Ntox47.st2.gian]: https://KristiPhammie.github.io/becr/html/Ntox47.st2.gian.html
[Stox_2]: https://KristiPhammie.github.io/becr/html/Stox_2.html
[STox_6]: https://KristiPhammie.github.io/becr/html/STox_6.html
[STox_11]: https://KristiPhammie.github.io/becr/html/STox_11_gian.html
[STox_11_kristi]: https://KristiPhammie.github.io/becr/html/STox_11_kristi.html
[STox_11.2]: https://KristiPhammie.github.io/becr/html/STox_11.2.html
[STox_11.3]: https://KristiPhammie.github.io/becr/html/STox_11.3.html
[STox_32_kristi]: https://KristiPhammie.github.io/becr/html/STox_32_kristi.html
[STox_39]: https://KristiPhammie.github.io/becr/html/STox_39_gian.html
[STox_39_kristi]: https://KristiPhammie.github.io/becr/html/STox_39_kristi.html
[STox_39.2]: https://KristiPhammie.github.io/becr/html/STox_39.2.html
[STox_57]: https://KristiPhammie.github.io/becr/html/STox_57.html
[STox_58]: https://KristiPhammie.github.io/becr/html/STox_58.html
[STox_59]: https://KristiPhammie.github.io/becr/html/STox_59.html
[YeeF_model]: https://KristiPhammie.github.io/becr/html/YeeF.html
[Barnase]: https://KristiPhammie.github.io/becr/html/Barnase.html
[Tox-Ribonuclease]: https://KristiPhammie.github.io/becr/html/Tox-Ribonuclease.html
[STox_1]: https://KristiPhammie.github.io/becr/html/STox_1.html
[STox_3]: https://KristiPhammie.github.io/becr/html/STox_3.html
[STox_4]: https://KristiPhammie.github.io/becr/html/STox_4.html
[STox_4.2]: https://KristiPhammie.github.io/becr/html/STox_4.2.html
[STox_55]: https://KristiPhammie.github.io/becr/html/STox_55.html
[BECR-Tox2]: https://KristiPhammie.github.io/becr/html/BECR-Tox2.html
[STox_37_gian]: https://KristiPhammie.github.io/becr/html/STox_37_gian.html
[STox_37]: https://KristiPhammie.github.io/becr/html/STox_37_kristi.html
[PBECR5_model]: https://KristiPhammie.github.io/becr/html/PBECR5.html
[Ntox48]: https://KristiPhammie.github.io/becr/html/Ntox48.html
[CdiA-CT_ECL_pfam]: https://KristiPhammie.github.io/becr/html/CdiA-CT_ECL_pfam.html
[CdiA-CT_ECL_kristi]: https://KristiPhammie.github.io/becr/html/CdiA-CT_ECL_kristi.html
[Ntox18.st1]: https://KristiPhammie.github.io/becr/html/Ntox18.st1.html
[Ntox18.st2]: https://KristiPhammie.github.io/becr/html/Ntox18.st2.html
[RNaseT1_model]: https://KristiPhammie.github.io/becr/html/RNaseT1.html
[RNaseT1.2]: https://KristiPhammie.github.io/becr/html/RNaseT1.2.html
[RNaseT1.3]: https://KristiPhammie.github.io/becr/html/RNaseT1.3.html
[Sarcin_model]: https://KristiPhammie.github.io/becr/html/Sarcin.html
[Sarcin_full_model]: https://KristiPhammie.github.io/becr/html/Sarcin_full.html


<!-- Molx snapshots -->
[BECR-Tox1_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BECR-Tox1.molx&snapshot-url-type=molx
[BECR-Tox3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BECR-Tox3.molx&snapshot-url-type=molx
[BECR-Tox4_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BECR-Tox4.molx&snapshot-url-type=molx
[ColicinD_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/ColicinD.molx&snapshot-url-type=molx
[ColicinD.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/ColicinD.2.molx&snapshot-url-type=molx
[ColicinE5_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/ColicinE5.molx&snapshot-url-type=molx
[CdiA-CT_Kp342_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/CdiA-CT_Kp342.molx&snapshot-url-type=molx
[CdiA-CT_EC3006_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/CdiA-CT_EC3006.molx&snapshot-url-type=molx
[CdiA-CT_EC869_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/CdiA-CT_EC869.molx&snapshot-url-type=molx
[CdiA-CT_NC101_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/CdiA-CT_NC101.molx&snapshot-url-type=molx
[CdiA-CT_96.154_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/CdiA-CT_96.154.molx&snapshot-url-type=molx
[DUF4258.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/DUF4258.2.molx&snapshot-url-type=molx
[DUF4258.3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/DUF4258.3.molx&snapshot-url-type=molx
[DUF4258.4_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/DUF4258.4.molx&snapshot-url-type=molx
[DUF4258.5_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/DUF4258.5.molx&snapshot-url-type=molx
[RNaseT2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RNaseT2.molx&snapshot-url-type=molx
[MuF-like_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/MuF-like.molx&snapshot-url-type=molx
[Ntox35_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox35.molx&snapshot-url-type=molx
[Ntox35.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox35.2.molx&snapshot-url-type=molx
[PBECR1_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/PBECR1.molx&snapshot-url-type=molx
[PBECR3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/PBECR3.molx&snapshot-url-type=molx
[PBECR3.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/PBECR3.2.molx&snapshot-url-type=molx
[PBECR4_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/PBECR4.molx&snapshot-url-type=molx
[PBECR4.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/PBECR4.2.molx&snapshot-url-type=molx
[Ntox19_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox19.molx&snapshot-url-type=molx
[Ntox49_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox49.molx&snapshot-url-type=molx
[RelE_E.coli_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RelE_E.coli.molx&snapshot-url-type=molx
[RelE_M.jannaschii_pdb_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RelE_M.jannaschii_pdb.molx&snapshot-url-type=molx
[RelE_M.jannaschii_afdb_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RelE_M.jannaschii_afdb.molx&snapshot-url-type=molx
[ParE_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/ParE.molx&snapshot-url-type=molx
[ParE.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/ParE.2.molx&snapshot-url-type=molx
[ParE.3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/ParE.3.molx&snapshot-url-type=molx
[ParE-like_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/ParE-like.molx&snapshot-url-type=molx
[YoeB_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/YoeB.molx&snapshot-url-type=molx
[YafO_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/YafO.molx&snapshot-url-type=molx
[YhaV_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/YhaV.molx&snapshot-url-type=molx
[HigB_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/HigB.molx&snapshot-url-type=molx
[HigB-like_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/HigB-like.molx&snapshot-url-type=molx
[BrnT_pdb_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BrnT_pdb.molx&snapshot-url-type=molx
[BrnT_afdb_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BrnT_afdb.molx&snapshot-url-type=molx
[BrnT.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BrnT.2.molx&snapshot-url-type=molx
[BrnT.3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BrnT.3.molx&snapshot-url-type=molx
[MqsR_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/MqsR.molx&snapshot-url-type=molx
[MqsR.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/MqsR.2.molx&snapshot-url-type=molx
[MqsR.3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/MqsR.3.molx&snapshot-url-type=molx
[YafQ_pdb_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/YafQ_pdb.molx&snapshot-url-type=molx
[YafQ_afdb_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/YafQ_afdb.molx&snapshot-url-type=molx
[gp49_pdb_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/gp49_pdb.molx&snapshot-url-type=molx
[gp49_afdb_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/gp49_afdb.molx&snapshot-url-type=molx
[RegB_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RegB.molx&snapshot-url-type=molx
[XendoU_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/XendoU.molx&snapshot-url-type=molx
[XendoU.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/XendoU.2.molx&snapshot-url-type=molx
[EndoU_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/EndoU.molx&snapshot-url-type=molx
[EndoU.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BECR-Tox5.molx&snapshot-url-type=molx
[EndoU.3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/EndoU.3.molx&snapshot-url-type=molx
[EndoU.4_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/EndoU.4.molx&snapshot-url-type=molx
[BC0920_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BC0920.molx&snapshot-url-type=molx
[STox_60_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_60.molx&snapshot-url-type=molx
[RNaseA_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RNaseA.molx&snapshot-url-type=molx
[RNaseA.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RNaseA.2.molx&snapshot-url-type=molx
[CdiA-CT_Ykris_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/CdiA-CT_Ykris.molx&snapshot-url-type=molx
[Ntox41_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox41.molx&snapshot-url-type=molx
[Ntox41.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox41.2.molx&snapshot-url-type=molx
[Ntox50_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox50.molx&snapshot-url-type=molx
[Ntox50.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox50.2.molx&snapshot-url-type=molx
[PF15657_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/PF15657.molx&snapshot-url-type=molx
[EndoVII.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/EndoVII.2.molx&snapshot-url-type=molx
[Ntox7_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox7.molx&snapshot-url-type=molx
[Ntox7.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox7.2.molx&snapshot-url-type=molx
[Ntox7.3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox7.3.molx&snapshot-url-type=molx
[Ntox36_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox36.molx&snapshot-url-type=molx
[Ntox47.st1_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox47.st1.molx&snapshot-url-type=molx
[Ntox47.st2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox47.st2.molx&snapshot-url-type=molx
[Stox_2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_2.molx&snapshot-url-type=molx
[STox_6_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_6.molx&snapshot-url-type=molx
[STox_11_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_11.molx&snapshot-url-type=molx
[STox_11.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_11.2.molx&snapshot-url-type=molx
[STox_11.3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_11.3.molx&snapshot-url-type=molx
[STox_32_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_32.molx&snapshot-url-type=molx
[STox_39_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_39.molx&snapshot-url-type=molx
[STox_39.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_39.2.molx&snapshot-url-type=molx
[STox_57_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_57.molx&snapshot-url-type=molx
[STox_58_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_58.molx&snapshot-url-type=molx
[STox_59_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_59.molx&snapshot-url-type=molx
[YeeF_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/YeeF.molx&snapshot-url-type=molx
[Barnase_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Barnase.molx&snapshot-url-type=molx
[Tox-Ribonuclease_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Tox-Ribonuclease.molx&snapshot-url-type=molx
[STox_1_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_1.molx&snapshot-url-type=molx
[STox_3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_3.molx&snapshot-url-type=molx
[STox_4_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_4.molx&snapshot-url-type=molx
[STox_4.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_4.2.molx&snapshot-url-type=molx
[STox_55_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_55.molx&snapshot-url-type=molx
[BECR-Tox2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/BECR-Tox2.molx&snapshot-url-type=molx
[STox_37_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/STox_37.molx&snapshot-url-type=molx
[PBECR5_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/PBECR5.molx&snapshot-url-type=molx
[Ntox48_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox48.molx&snapshot-url-type=molx
[CdiA-CT_ECL_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/CdiA-CT_ECL.molx&snapshot-url-type=molx
[Ntox18.st1_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox18.st1.molx&snapshot-url-type=molx
[Ntox18.st2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Ntox18.st2.molx&snapshot-url-type=molx
[RNaseT1_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RNase_T1.molx&snapshot-url-type=molx
[RNaseT1.2_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RNaseT1.2.molx&snapshot-url-type=molx
[RNaseT1.3_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/RNaseT1.3.molx&snapshot-url-type=molx
[Sarcin_molx]: https://molstar.org/viewer/?snapshot-url=https://KristiPhammie.github.io/becr/molx/Sarcin.molx&snapshot-url-type=molx

## HMM Models

- [BC_0920.hmm]:
- [BECR-Tox1.hmm][BECR-Tox1_hmm]
- [BECR-Tox2.hmm][BECR-Tox2_hmm]
- [BECR-Tox3.hmm][BECR-Tox3_hmm]
- [BECR-Tox4.hmm][BECR-Tox4_hmm]
- [BECR-Tox5.hmm][BECR-Tox5_hmm]
- [BECR-like-Tox1.2.hmm][BECR-like-Tox1.2_hmm]
- [Barnase.hmm][Barnase_hmm]
- [BrnT.hmm][BrnT_hmm]
- [BrnT.2.hmm][BrnT.2_hmm]
- [BrnT.3.hmm][BrnT.3_hmm]
- [CdiA-CT_96.154.hmm][CdiA-CT_96.154_hmm]
- [CdiA-CT_EC3006.hmm][CdiA-CT_EC3006_hmm]
- [CdiA-CT_EC869.hmm][CdiA-CT_EC869_hmm]
- [CdiA-CT_ECL.hmm][CdiA-CT_ECL_hmm]
- [CdiA-CT_Kp342.hmm][CdiA-CT_Kp342_hmm]
- [CdiA-CT_NC101.hmm][CdiA-CT_NC101_hmm]
- [CdiA-CT_Ykris.hmm][CdiA-CT_Ykris_hmm]
- [ColicinD.hmm][ColicinD_hmm]
- [ColicinD.2.hmm][ColicinD.2_hmm]
- [ColicinE3.hmm][ColicinE3_hmm]
- [ColicinE5.hmm][ColicinE5_hmm]
- [EndoU.hmm][EndoU_hmm]
- [EndoU.3.hmm][EndoU.3_hmm]
- [EndoU.4.hmm][EndoU.4_hmm]
- [EndoVII.hmm][EndoVII_hmm]
- [HigB.hmm][HigB_hmm]
- [HigB-like.hmm][HigB-like_hmm]
- [MafB.hmm][MafB_hmm]
- [MqsR.hmm][MqsR_hmm]
- [MqsR.2.hmm][MqsR.2_hmm]
- [MqsR.3.hmm][MqsR.3_hmm]
- [MuF-like.hmm][MuF-like_hmm]
- [Ntox18.st1.hmm][Ntox18.st1_hmm]
- [Ntox18.st2.hmm][Ntox18.st2_hmm]
- [Ntox19.st.hmm][Ntox19.st_hmm]
- [Ntox21.hmm][Ntox21_hmm]
- [Ntox35.hmm][Ntox35_hmm]
- [Ntox35.2.hmm][Ntox35.2_hmm]
- [Ntox36.hmm][Ntox36_hmm]
- [Ntox41.hmm][Ntox41_hmm]
- [Ntox41.2.hmm][Ntox41.2_hmm]
- [Ntox47.st1.hmm][Ntox47.st1_hmm]
- [Ntox47.st2.hmm][Ntox47.st2_hmm]
- [Ntox47_PF15540.hmm][Ntox47_PF15540_hmm]
- [Ntox48.hmm][Ntox48_hmm]
- [Ntox49.2.hmm][Ntox49.2_hmm]
- [Ntox49.3.hmm][Ntox49.3_hmm]
- [Ntox49.4.hmm][Ntox49.4_hmm]
- [Ntox49.5.hmm][Ntox49.5_hmm]
- [Ntox49.st.hmm][Ntox49.st_hmm]
- [Ntox50.hmm][Ntox50_hmm]
- [Ntox50.2.hmm][Ntox50.2_hmm]
- [Ntox7.2.hmm][Ntox7.2_hmm]
- [Ntox7.3.hmm][Ntox7.3_hmm]
- [Ntox7.st.hmm][Ntox7.st_hmm]
- [PBECR1.hmm][PBECR1_hmm]
- [PBECR3.hmm][PBECR3_hmm]
- [PBECR3.2.hmm][PBECR3.2_hmm]
- [PBECR4.hmm][PBECR4_hmm]
- [PBECR4.2.hmm][PBECR4.2_hmm]
- [PBECR5.hmm][PBECR5_hmm]
- [ParE.hmm][ParE_hmm]
- [ParE-like.hmm][ParE-like_hmm]
- [ParE.2.hmm][ParE.2_hmm]
- [ParE.3.hmm][ParE.3_hmm]
- [RNaseA.hmm][RNaseA_hmm]
- [RNaseA.2.hmm][RNaseA.2_hmm]
- [RNaseT1.hmm][RNaseT1_hmm]
- [RNaseT1.2.hmm][RNaseT1.2_hmm]
- [RNaseT1.3.hmm][RNaseT1.3_hmm]
- [RNaseT2.hmm][RNaseT2_hmm]
- [RegB.hmm][RegB_hmm]
- [RelE_E.coli.hmm][RelE_E.coli_hmm]
- [RelE_M.jannaschii.hmm][RelE_M.jannaschii_hmm]
- [STox_1.hmm][STox_1_hmm]
- [STox_11.hmm][STox_11_hmm]
- [STox_11.2.hmm][STox_11.2_hmm]
- [STox_11.3.hmm][STox_11.3_hmm]
- [STox_2.hmm][STox_2_hmm]
- [STox_3.hmm][STox_3_hmm]
- [STox_32.hmm][STox_32_hmm]
- [STox_37.hmm][STox_37_hmm]
- [STox_39.hmm][STox_39_hmm]
- [STox_39.2.hmm][STox_39.2_hmm]
- [STox_4.hmm][STox_4_hmm]
- [STox_4.2.hmm][STox_4.2_hmm]
- [STox_55.hmm][STox_55_hmm]
- [STox_57.hmm][STox_57_hmm]
- [STox_58.hmm][STox_58_hmm]
- [STox_59.hmm][STox_59_hmm]
- [STox_6.hmm][STox_6_hmm]
- [STox_60.hmm][STox_60_hmm]
- [Sarcin.hmm][Sarcin_hmm]
- [Tox-Ribonuclease.hmm][Tox-Ribonuclease_hmm]
- [XendoU.hmm][XendoU_hmm]
- [XendoU.2.hmm][XendoU.2_hmm]
- [YafO.hmm][YafO_hmm]
- [YafQ.hmm][YafQ_hmm]
- [YeeF.hmm][YeeF_hmm]
- [YhaV.hmm][YhaV_hmm]
- [YoeB.hmm][YoeB_hmm]
- [gp49.hmm][gp49_hmm]

## HHM Models

- [BC_0920.hhm][BC_0920_hhm]
- [BECR-Tox1.hhm][BECR-Tox1_hhm]
- [BECR-Tox2.hhm][BECR-Tox2_hhm]
- [BECR-Tox3.hhm][BECR-Tox3_hhm]
- [BECR-Tox4.hhm][BECR-Tox4_hhm]
- [BECR-Tox5.hhm][BECR-Tox5_hhm]
- [BECR-like-Tox1.2.hhm][BECR-like-Tox1.2_hhm]
- [Barnase.hhm][Barnase_hhm]
- [BrnT.hhm][BrnT_hhm]
- [BrnT.2.hhm][BrnT.2_hhm]
- [BrnT.3.hhm][BrnT.3_hhm]
- [CdiA-CT_96.154.hhm][CdiA-CT_96.154_hhm]
- [CdiA-CT_EC3006.hhm][CdiA-CT_EC3006_hhm]
- [CdiA-CT_EC869.hhm][CdiA-CT_EC869_hhm]
- [CdiA-CT_ECL.hhm][CdiA-CT_ECL_hhm]
- [CdiA-CT_Kp342.hhm][CdiA-CT_Kp342_hhm]
- [CdiA-CT_NC101.hhm][CdiA-CT_NC101_hhm]
- [CdiA-CT_Ykris.hhm][CdiA-CT_Ykris_hhm]
- [ColicinD.hhm][ColicinD_hhm]
- [ColicinD.2.hhm][ColicinD.2_hhm]
- [ColicinE3.hhm][ColicinE3_hhm]
- [ColicinE5.hhm][ColicinE5_hhm]
- [EndoU.hhm][EndoU_hhm]
- [EndoU.3.hhm][EndoU.3_hhm]
- [EndoU.4.hhm][EndoU.4_hhm]
- [EndoVII.hhm][EndoVII_hhm]
- [HigB.hhm][HigB_hhm]
- [HigB-like.hhm][HigB-like_hhm]
- [MafB.hhm][MafB_hhm]
- [MqsR.hhm][MqsR_hhm]
- [MqsR.2.hhm][MqsR.2_hhm]
- [MqsR.3.hhm][MqsR.3_hhm]
- [MuF-like.hhm][MuF-like_hhm]
- [Ntox18.st1.hhm][Ntox18.st1_hhm]
- [Ntox18.st2.hhm][Ntox18.st2_hhm]
- [Ntox19.st.hhm][Ntox19.st_hhm]
- [Ntox21.hhm][Ntox21_hhm]
- [Ntox35.hhm][Ntox35_hhm]
- [Ntox35.2.hhm][Ntox35.2_hhm]
- [Ntox36.hhm][Ntox36_hhm]
- [Ntox41.hhm][Ntox41_hhm]
- [Ntox41.2.hhm][Ntox41.2_hhm]
- [Ntox47.st1.hhm][Ntox47.st1_hhm]
- [Ntox47.st2.hhm][Ntox47.st2_hhm]
- [Ntox47_PF15540.hhm][Ntox47_PF15540_hhm]
- [Ntox49.2.hhm][Ntox49.2_hhm]
- [Ntox49.3.hhm][Ntox49.3_hhm]
- [Ntox49.4.hhm][Ntox49.4_hhm]
- [Ntox49.5.hhm][Ntox49.5_hhm]
- [Ntox49.st.hhm][Ntox49.st_hhm]
- [Ntox50.hhm][Ntox50_hhm]
- [Ntox50.2.hhm][Ntox50.2_hhm]
- [Ntox7.2.hhm][Ntox7.2_hhm]
- [Ntox7.3.hhm][Ntox7.3_hhm]
- [Ntox7.st.hhm][Ntox7.st_hhm]
- [PBECR1.hhm][PBECR1_hhm]
- [PBECR3.hhm][PBECR3_hhm]
- [PBECR3.2.hhm][PBECR3.2_hhm]
- [PBECR4.hhm][PBECR4_hhm]
- [PBECR4.2.hhm][PBECR4.2_hhm]
- [PBECR5.hhm][PBECR5_hhm]
- [ParE.hhm][ParE_hhm]
- [ParE-like.hhm][ParE-like_hhm]
- [ParE.2.hhm][ParE.2_hhm]
- [ParE.3.hhm][ParE.3_hhm]
- [RNaseA.hhm][RNaseA_hhm]
- [RNaseA.2.hhm][RNaseA.2_hhm]
- [RNaseT1.hhm][RNaseT1_hhm]
- [RNaseT1.2.hhm][RNaseT1.2_hhm]
- [RNaseT1.3.hhm][RNaseT1.3_hhm]
- [RNaseT2.hhm][RNaseT2_hhm]
- [RegB.hhm][RegB_hhm]
- [RelE_E.coli.hhm][RelE_E.coli_hhm]
- [RelE_M.jannaschii.hhm][RelE_M.jannaschii_hhm]
- [STox_1.hhm][STox_1_hhm]
- [STox_11.hhm][STox_11_hhm]
- [STox_11.2.hhm][STox_11.2_hhm]
- [STox_11.3.hhm][STox_11.3_hhm]
- [STox_2.hhm][STox_2_hhm]
- [STox_3.hhm][STox_3_hhm]
- [STox_32.hhm][STox_32_hhm]
- [STox_37.hhm][STox_37_hhm]
- [STox_39.hhm][STox_39_hhm]
- [STox_39.2.hhm][STox_39.2_hhm]
- [STox_4.hhm][STox_4_hhm]
- [STox_4.2.hhm][STox_4.2_hhm]
- [STox_55.hhm][STox_55_hhm]
- [STox_57.hhm][STox_57_hhm]
- [STox_58.hhm][STox_58_hhm]
- [STox_59.hhm][STox_59_hhm]
- [STox_6.hhm][STox_6_hhm]
- [STox_60.hhm][STox_60_hhm]
- [Sarcin.hhm][Sarcin_hhm]
- [Tox-Ribonuclease.hhm][Tox-Ribonuclease_hhm]
- [XendoU.hhm][XendoU_hhm]
- [XendoU.2.hhm][XendoU.2_hhm]
- [YafO.hhm][YafO_hhm]
- [YafQ.hhm][YafQ_hhm]
- [YeeF.hhm][YeeF_hhm]
- [YhaV.hhm][YhaV_hhm]
- [YoeB.hhm][YoeB_hhm]
- [gp49.hhm][gp49_hhm]


[BC_0920_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BC_0920.hmm
[BECR-Tox1_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BECR-Tox1.hmm
[BECR-Tox2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BECR-Tox2.hmm
[BECR-Tox3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BECR-Tox3.hmm
[BECR-Tox4_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BECR-Tox4.hmm
[BECR-Tox5_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BECR-Tox5.hmm
[BECR-like-Tox1.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BECR-like-Tox1.2.hmm
[Barnase_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Barnase.hmm
[BrnT_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BrnT.hmm
[BrnT.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BrnT.2.hmm
[BrnT.3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/BrnT.3.hmm
[CdiA-CT_96.154_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/CdiA-CT_96.154.hmm
[CdiA-CT_EC3006_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/CdiA-CT_EC3006.hmm
[CdiA-CT_EC869_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/CdiA-CT_EC869.hmm
[CdiA-CT_ECL_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/CdiA-CT_ECL.hmm
[CdiA-CT_Kp342_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/CdiA-CT_Kp342.hmm
[CdiA-CT_NC101_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/CdiA-CT_NC101.hmm
[CdiA-CT_Ykris_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/CdiA-CT_Ykris.hmm
[ColicinD_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/ColicinD.hmm
[ColicinD.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/ColicinD.2.hmm
[ColicinE3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/ColicinE3.hmm
[ColicinE5_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/ColicinE5.hmm
[EndoU_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/EndoU.hmm
[EndoU.3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/EndoU.3.hmm
[EndoU.4_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/EndoU.4.hmm
[EndoVII_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/EndoVII.hmm
[HigB_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/HigB.hmm
[HigB-like_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/HigB-like.hmm
[MafB_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/MafB.hmm
[MqsR_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/MqsR.hmm
[MqsR.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/MqsR.2.hmm
[MqsR.3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/MqsR.3.hmm
[MuF-like_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/MuF-like.hmm
[Ntox18.st1_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox18.st1.hmm
[Ntox18.st2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox18.st2.hmm
[Ntox19.st_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox19.st.hmm
[Ntox21_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox21.hmm
[Ntox35_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox35.hmm
[Ntox35.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox35.2.hmm
[Ntox36_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox36.hmm
[Ntox41_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox41.hmm
[Ntox41.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox41.2.hmm
[Ntox47.st1_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox47.st1.hmm
[Ntox47.st2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox47.st2.hmm
[Ntox47_PF15540_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox47_PF15540.hmm
[Ntox48_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox48.hmm
[Ntox49.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox49.2.hmm
[Ntox49.3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox49.3.hmm
[Ntox49.4_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox49.4.hmm
[Ntox49.5_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox49.5.hmm
[Ntox49.st_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox49.st.hmm
[Ntox50_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox50.hmm
[Ntox50.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox50.2.hmm
[Ntox7.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox7.2.hmm
[Ntox7.3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox7.3.hmm
[Ntox7.st_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Ntox7.st.hmm
[PBECR1_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/PBECR1.hmm
[PBECR3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/PBECR3.hmm
[PBECR3.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/PBECR3.2.hmm
[PBECR4_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/PBECR4.hmm
[PBECR4.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/PBECR4.2.hmm
[PBECR5_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/PBECR5.hmm
[ParE_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/ParE.hmm
[ParE-like_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/ParE-like.hmm
[ParE.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/ParE.2.hmm
[ParE.3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/ParE.3.hmm
[RNaseA_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/RNaseA.hmm
[RNaseA.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/RNaseA.2.hmm
[RNaseT1_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/RNaseT1.hmm
[RNaseT1.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/RNaseT1.2.hmm
[RNaseT1.3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/RNaseT1.3.hmm
[RNaseT2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/RNaseT2.hmm
[RegB_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/RegB.hmm
[RelE_E.coli_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/RelE_E.coli.hmm
[RelE_M.jannaschii_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/RelE_M.jannaschii.hmm
[STox_1_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_1.hmm
[STox_11_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_11.hmm
[STox_11.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_11.2.hmm
[STox_11.3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_11.3.hmm
[STox_2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_2.hmm
[STox_3_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_3.hmm
[STox_32_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_32.hmm
[STox_37_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_37.hmm
[STox_39_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_39.hmm
[STox_39.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_39.2.hmm
[STox_4_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_4.hmm
[STox_4.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_4.2.hmm
[STox_55_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_55.hmm
[STox_57_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_57.hmm
[STox_58_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_58.hmm
[STox_59_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_59.hmm
[STox_6_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_6.hmm
[STox_60_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/STox_60.hmm
[Sarcin_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Sarcin.hmm
[Tox-Ribonuclease_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/Tox-Ribonuclease.hmm
[XendoU_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/XendoU.hmm
[XendoU.2_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/XendoU.2.hmm
[YafO_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/YafO.hmm
[YafQ_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/YafQ.hmm
[YeeF_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/YeeF.hmm
[YhaV_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/YhaV.hmm
[YoeB_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/YoeB.hmm
[gp49_hmm]: https://github.com/KristiPhammie/becr/blob/main/hmm/gp49.hmm
[BC_0920_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BC_0920.hhm
[BECR-Tox1_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BECR-Tox1.hhm
[BECR-Tox2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BECR-Tox2.hhm
[BECR-Tox3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BECR-Tox3.hhm
[BECR-Tox4_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BECR-Tox4.hhm
[BECR-Tox5_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BECR-Tox5.hhm
[BECR-like-Tox1.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BECR-like-Tox1.2.hhm
[Barnase_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Barnase.hhm
[BrnT_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BrnT.hhm
[BrnT.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BrnT.2.hhm
[BrnT.3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/BrnT.3.hhm
[CdiA-CT_96.154_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/CdiA-CT_96.154.hhm
[CdiA-CT_EC3006_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/CdiA-CT_EC3006.hhm
[CdiA-CT_EC869_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/CdiA-CT_EC869.hhm
[CdiA-CT_ECL_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/CdiA-CT_ECL.hhm
[CdiA-CT_Kp342_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/CdiA-CT_Kp342.hhm
[CdiA-CT_NC101_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/CdiA-CT_NC101.hhm
[CdiA-CT_Ykris_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/CdiA-CT_Ykris.hhm
[ColicinD_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/ColicinD.hhm
[ColicinD.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/ColicinD.2.hhm
[ColicinE3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/ColicinE3.hhm
[ColicinE5_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/ColicinE5.hhm
[EndoU_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/EndoU.hhm
[EndoU.3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/EndoU.3.hhm
[EndoU.4_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/EndoU.4.hhm
[EndoVII_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/EndoVII.hhm
[HigB_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/HigB.hhm
[HigB-like_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/HigB-like.hhm
[MafB_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/MafB.hhm
[MqsR_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/MqsR.hhm
[MqsR.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/MqsR.2.hhm
[MqsR.3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/MqsR.3.hhm
[MuF-like_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/MuF-like.hhm
[Ntox18.st1_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox18.st1.hhm
[Ntox18.st2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox18.st2.hhm
[Ntox19.st_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox19.st.hhm
[Ntox21_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox21.hhm
[Ntox35_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox35.hhm
[Ntox35.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox35.2.hhm
[Ntox36_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox36.hhm
[Ntox41_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox41.hhm
[Ntox41.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox41.2.hhm
[Ntox47.st1_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox47.st1.hhm
[Ntox47.st2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox47.st2.hhm
[Ntox47_PF15540_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox47_PF15540.hhm
[Ntox49.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox49.2.hhm
[Ntox49.3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox49.3.hhm
[Ntox49.4_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox49.4.hhm
[Ntox49.5_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox49.5.hhm
[Ntox49.st_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox49.st.hhm
[Ntox50_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox50.hhm
[Ntox50.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox50.2.hhm
[Ntox7.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox7.2.hhm
[Ntox7.3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox7.3.hhm
[Ntox7.st_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Ntox7.st.hhm
[PBECR1_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/PBECR1.hhm
[PBECR3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/PBECR3.hhm
[PBECR3.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/PBECR3.2.hhm
[PBECR4_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/PBECR4.hhm
[PBECR4.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/PBECR4.2.hhm
[PBECR5_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/PBECR5.hhm
[ParE_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/ParE.hhm
[ParE-like_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/ParE-like.hhm
[ParE.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/ParE.2.hhm
[ParE.3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/ParE.3.hhm
[RNaseA_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/RNaseA.hhm
[RNaseA.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/RNaseA.2.hhm
[RNaseT1_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/RNaseT1.hhm
[RNaseT1.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/RNaseT1.2.hhm
[RNaseT1.3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/RNaseT1.3.hhm
[RNaseT2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/RNaseT2.hhm
[RegB_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/RegB.hhm
[RelE_E.coli_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/RelE_E.coli.hhm
[RelE_M.jannaschii_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/RelE_M.jannaschii.hhm
[STox_1_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_1.hhm
[STox_11_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_11.hhm
[STox_11.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_11.2.hhm
[STox_11.3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_11.3.hhm
[STox_2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_2.hhm
[STox_3_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_3.hhm
[STox_32_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_32.hhm
[STox_37_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_37.hhm
[STox_39_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_39.hhm
[STox_39.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_39.2.hhm
[STox_4_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_4.hhm
[STox_4.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_4.2.hhm
[STox_55_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_55.hhm
[STox_57_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_57.hhm
[STox_58_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_58.hhm
[STox_59_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_59.hhm
[STox_6_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_6.hhm
[STox_60_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/STox_60.hhm
[Sarcin_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Sarcin.hhm
[Tox-Ribonuclease_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/Tox-Ribonuclease.hhm
[XendoU_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/XendoU.hhm
[XendoU.2_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/XendoU.2.hhm
[YafO_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/YafO.hhm
[YafQ_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/YafQ.hhm
[YeeF_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/YeeF.hhm
[YhaV_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/YhaV.hhm
[YoeB_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/YoeB.hhm
[gp49_hhm]: https://github.com/KristiPhammie/becr/blob/main/hhm/gp49.hhm
