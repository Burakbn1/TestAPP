class tum_degerler_tutma():

    global glob_testno        
    global glob_reportno
    global glob_typeTest
    global glob_manufacturer
    global glob_client
    global glob_testobject
    global glob_paneltype
    global glob_rV
    global glob_rp
    global glob_ra
    global glob_rc
    global glob_rf
    global glob_rt
    global glob_tc
    global glob_reportdate
    global glob_rliv
    global glob_rpfv
    global glob_iac
    global glob_iat
    global glob_ctins
    global glob_busbar
    global glob_cable

    def test_no_alma_func(testno):
        glob_testno= testno
        print(glob_testno)

        
    def gelen_deger_tutma_ilk_sayfa(testno, reportno, typeTest, manufacturer, client, testobject, paneltype,rV,rp,ra,rc,rf,rt,tc,reportdate,rliv,rpfv, iac, iat, ctins, busbar,cable):
    
        glob_reportno= reportno
        glob_typeTest= typeTest
        glob_manufacturer= manufacturer
        glob_client= client
        glob_testobject= testobject
        glob_paneltype= paneltype
        glob_rV= rV
        glob_rp= rp
        glob_ra= ra
        glob_rc= rc
        glob_rf= rf
        glob_rt= rt
        glob_tc= tc
        glob_reportdate= reportdate
        glob_rliv=rliv       
        glob_rpfv= rpfv
        glob_iac= iac
        glob_iat= iat
        glob_ctins= ctins
        glob_busbar= busbar
        glob_cable= cable


        print(glob_reportno, glob_typeTest, glob_manufacturer, glob_client, glob_testobject, glob_paneltype, glob_rV, glob_rp)

    