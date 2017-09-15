import pytest
import os, sys, logging

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

htmlReportPath = "C:\\Users\\manish2\\Documents\\LiClipse_Workspace\\Rough_WorkSpace\\Src\\Com\\Reports\\htmlTestReport.html"
xmlReportPath = "C:\\Users\\manish2\\Documents\\LiClipse_Workspace\\Rough_WorkSpace\\Src\\Com\\Reports\\xmlTestReport.xml"

# path1 = os.getcwd()
htmlpath = os.path.join(os.getcwd(),"Src\\Com\\Reports\\htmlTestReport.html")
htmlReportPath = os.path.normpath(htmlpath)
xmlpath = os.path.join(os.getcwd(),"Src\\Com\\Reports\\xmlTestReport.xml")
xmlReportPath = os.path.normpath(xmlpath)
logging.info(htmlReportPath)
logging.info(xmlReportPath)

# pytest.main(["--junit-xml=C:\Users\manish2\Documents\LiClipse Workspace\Prj","-s","-v", "--pyargs", "Com.Testcases.Test_RoughWork"])
pytest.main(["--html="+htmlReportPath,"--junitxml="+xmlReportPath,"-s", "-v", "--pyargs", "Src.Com.Testcases.Test_Pyspark"])
