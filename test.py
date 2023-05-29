import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

JS_DROP_FILE = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"

base_url = 'https://js-55fbfg.stackblitz.io/'
project_root = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Chrome(executable_path='C:\\Users\\dvale\\Documents\\QAAutomation\\Taxer\\chromedriver.exe')
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

button_run_this_project = driver.find_element(By.XPATH, '//button[@onclick="__runProject()"]')
button_run_this_project.click()

button_add = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')


def add_cert(line_num, cert_file_name):
    button_add.click()
    path = project_root + '\\certs\\' + cert_file_name
    target = driver.find_element(By.XPATH, '//div[@class="card dropbox-panel"]')
    file_input = driver.execute_script(JS_DROP_FILE, target, 0, 0)
    file_input.send_keys(path)


def get_list_item(line_num):
    return driver.find_element(By.XPATH, '//div[@class="list-group mb-3"]/a[' + str(line_num) + ']')


def assert_cert(line_num, data):
    list_item = get_list_item(line_num)
    assert list_item.text == data[0]
    subject_cn = driver.find_element(By.XPATH, '//div[@class="card-body"]//tr[1]/td')
    assert subject_cn.text == data[0]
    issuer_cn = driver.find_element(By.XPATH, '//div[@class="card-body"]//tr[2]/td')
    assert issuer_cn.text == data[1]
    valid_from = driver.find_element(By.XPATH, '//div[@class="card-body"]//tr[3]/td')
    assert valid_from.text == data[2]
    valid_till = driver.find_element(By.XPATH, '//div[@class="card-body"]//tr[4]/td')
    assert valid_till.text == data[3]
    time.sleep(1)


cert1_data = ('Таксер Тест Тестерович', 'UA-22723472', '2015-04-08 21:00:00 UTC', '2017-04-08 21:00:00 UTC')
cert2_data = ('Лиференко', 'UA-39787008-2015', '2017-12-26 13:13:27 UTC', '2018-12-26 13:13:27 UTC')
cert3_data = ('UA-00015622-2017', 'UA-00015622-2017', '2017-09-22 07:19:00 UTC', '2027-09-22 07:19:00 UTC')

add_cert(1, 'cert.cer')
assert_cert(1, cert1_data)
print('Step 1 passed')

add_cert(2, 'cert2.cer')
assert_cert(2, cert2_data)
print('Step 2 passed')

add_cert(3, 'czo_2017.cer')
assert_cert(3, cert3_data)
print('Step 3 passed')

get_list_item(1).click()
assert_cert(1, cert1_data)
print('Step 4 passed')

get_list_item(2).click()
assert_cert(2, cert2_data)
print('Step 5 passed')

get_list_item(3).click()
assert_cert(3, cert3_data)
print('Step 6 passed')

driver.refresh()
time.sleep(5)
get_list_item(1).click()
assert_cert(1, cert1_data)
print('Step 7 passed')

get_list_item(2).click()
assert_cert(2, cert2_data)
print('Step 8 passed')

get_list_item(3).click()
assert_cert(3, cert3_data)
print('Step 9 passed')

time.sleep(10)
