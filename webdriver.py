from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def fillOutForm(arName, arType, arLevel, arMain, arSub):

    '''
        recieve 5 param
        1. Name of artifact
        2. Type of artifact
        3. Level of artifact
        4. Main stat of artifact
        5. 4 sub stat of artifact
    '''

    options = webdriver.chrome.options.Options()
    options.add_argument('--user-data-dir=C:/Users/USER/AppData/Local/Google/Chrome/User Data')
    options.add_argument('--disable-extensions')

    # init webdriver
    web = webdriver.Chrome(executable_path='C:/Program Files/ChromeDriver/chromedriver.exe', chrome_options=options)

    # WebDriverWait(web, 10).until(web.find)

    # route to the web
    web.get('https://frzyc.github.io/genshin-optimizer/#/artifact')

    # ------------- Name of artifact -----------------

    # activate artifact name dropdown
    artifact_name_button = web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/button')
    artifact_name_button.click()

    # indicate dropdown element
    artifact_name_dropdown_parent = web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div')

    # create artifact name list from parent
    artifact_name_dropdown_list = artifact_name_dropdown_parent.find_elements_by_tag_name('a')

    selected_name_artifact = list(filter(lambda x: x.text == 'Noblesse Oblige', artifact_name_dropdown_list))[0]
    selected_name_artifact.click()

    # ------------- Type of artifact -----------------

    # activate artifact type dropdown
    artifact_type_button = web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/button')
    artifact_type_button.click()

    # indicate dropdown element
    artifact_type_dropdown_parent = web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/div')

    # create artifact type list from parent
    artifact_type_dropdown_list = artifact_type_dropdown_parent.find_elements_by_tag_name('span')

    selected_type_artifact = list(filter(lambda x: x.text == arType, artifact_type_dropdown_list))[0]
    selected_type_artifact.click()


    # ------------- Level of artifact -----------------

    level_artifact_input = web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/input')
    level_artifact_input.send_keys(Keys.BACK_SPACE, arLevel)

    # ------------- Main stat of artifact -----------------

    main_stat_button = web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/button')
    main_stat_button.click()

    # check if type of artifact is not flower/feather

    main_stat_dropdown_parent = web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div')

    # create artifact type list from parent
    main_stat_dropdown_list = main_stat_dropdown_parent.find_elements_by_tag_name('a')

    selected_main_stat = list(filter(lambda x: x.text == arMain, main_stat_dropdown_list))[0]
    selected_main_stat.click()

    # ------------- 4 sub stat of artifact -----------------

    sub_stats = []
    sub_vals = []
    for i in range(len(arSub)):
        sub_stats.append(list(arSub[i].keys())[0])
        sub_vals.append(list(arSub[i].values())[0])

    print(sub_stats, sub_vals)

    sub_stat_parent = web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[2]')

    sub_stat_button_list = sub_stat_parent.find_elements_by_tag_name('button')

    sub_stat_input_list = sub_stat_parent.find_elements_by_tag_name('input')

    for i in range(len(sub_stat_button_list)):
        
        sub_stat_button_list[i].click()

        sub_stat_dropdown = sub_stat_parent.find_elements_by_css_selector('.dropdown-menu')
        sub_stat_dropdown_list = sub_stat_dropdown[i].find_elements_by_tag_name('a')
        
        selected_main_stat = list(filter(lambda x: x.text == sub_stats[i], sub_stat_dropdown_list))[0]
        selected_main_stat.click()

        sub_stat_input_list[i].send_keys(sub_vals[i], Keys.ENTER)

    # ------------- submit -----------------

    submit_button = web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[3]/button[1]')
    submit_button.click()
