import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\dvale\\Documents\\QAAutomation\\Taxer\\chromedriver.exe')
base_url = 'https://js-55fbfg.stackblitz.io/'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

button_run_this_project = driver.find_element(By.XPATH, '//button[@onclick="__runProject()"]')
button_run_this_project.click()

button_add = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
button_add.click()

JS_DROP_FILE = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"

project_root = os.path.dirname(os.path.abspath(__file__))

path_cert_1 = project_root + '\\cert.cer'
target = driver.find_element(By.XPATH, '//div[@class="card dropbox-panel"]')


def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)


drag_and_drop_file(target, path_cert_1)

cert_1_text = driver.find_element(By.XPATH,"//a[@href='javascript:void(0)']")
value_cert_1_text = cert_1_text.text
assert value_cert_1_text == 'Таксер Тест Тестерович'
print('Pass 1')


button_add.click()
path_cert_2 = project_root + '\\cert2.cer'
drag_and_drop_file(target, path_cert_2)
cert_2_text = driver.find_element(By.XPATH, '//a[@href="javascript:void(0)"][2]')
value_cert_2_text = cert_2_text.text
assert value_cert_2_text == 'Лиференко'
print('Pass 2')


button_add.click()
path_cert_3 = project_root + '\\czo_2017.cer'
drag_and_drop_file(target, path_cert_3)
cert_3_text = driver.find_element(By.XPATH, '//a[@href="javascript:void(0)"][3]')
value_cert_3_text = cert_3_text.text
assert value_cert_3_text == 'UA-00015622-2017'
print('Pass 3')
time.sleep(10)