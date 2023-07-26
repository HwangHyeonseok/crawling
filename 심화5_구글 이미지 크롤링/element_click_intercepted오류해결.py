img.click() #셀레니움 클릭 방식대신
browser.execute_script("arguments[0].click();", img) # javascript로 클릭하도록 한다.