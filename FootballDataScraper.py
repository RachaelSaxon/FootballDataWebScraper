#import packages
import requests
from bs4 import BeautifulSoup
import lxml.html as lh 
import pandas as pd
import openpyxl
from selenium import webdriver
from pandas.io.html import read_html 
#start getting tables
#Overall table
driver = webdriver.Safari()
driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_results32321_overall')
table_html = table.get_attribute('innerHTML')
lt_df = read_html(table_html)[0]
#lt_df.columns = lt_df.columns.get_level_values(1)
#driver.close()
#Home Away Table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_results32321_home_away')
table_html = table.get_attribute('innerHTML')
homeaway_df = read_html(table_html)[0]
homeaway_df.columns = homeaway_df.columns.get_level_values(1)
#driver.close()
#Squads table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_standard_squads')
table_html = table.get_attribute('innerHTML')
squads_df = read_html(table_html)[0]
squads_df.columns = squads_df.columns.get_level_values(1)
#driver.close()
#Keeper table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_keeper_squads')
table_html = table.get_attribute('innerHTML')
keeper_df = read_html(table_html)[0]
keeper_df.columns = keeper_df.columns.get_level_values(1)
#driver.close()
#Keeper advanced table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_keeper_adv_squads')
table_html = table.get_attribute('innerHTML')
keeperadv_df = read_html(table_html)[0]
keeperadv_df.columns = keeperadv_df.columns.get_level_values(1)
#driver.close()
#Shooting table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_shooting_squads')
table_html = table.get_attribute('innerHTML')
shooting_df = read_html(table_html)[0]
shooting_df.columns = shooting_df.columns.get_level_values(1)
#driver.close()
#Passing table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_passing_squads')
table_html = table.get_attribute('innerHTML')
passing_df = read_html(table_html)[0]
passing_df.columns = passing_df.columns.get_level_values(1)
#driver.close()
#Passing types table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_passing_types_squads')
table_html = table.get_attribute('innerHTML')
passingtypes_df = read_html(table_html)[0]
passingtypes_df.columns = passingtypes_df.columns.get_level_values(1)
#driver.close()
#GCA table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_gca_squads')
table_html = table.get_attribute('innerHTML')
gca_df = read_html(table_html)[0]
gca_df.columns = gca_df.columns.get_level_values(1)
#driver.close()
#Defense table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_defense_squads')
table_html = table.get_attribute('innerHTML')
defense_df = read_html(table_html)[0]
defense_df.columns = defense_df.columns.get_level_values(1)
#driver.close()
#Possession table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_possession_squads')
table_html = table.get_attribute('innerHTML')
possession_df = read_html(table_html)[0]
possession_df.columns = possession_df.columns.get_level_values(1)
#driver.close()
#Playing time table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_playing_time_squads')
table_html = table.get_attribute('innerHTML')
playingtime_df = read_html(table_html)[0]
playingtime_df.columns = playingtime_df.columns.get_level_values(1)
#driver.close()
#Miscellaneous table
#driver = webdriver.Safari()
#driver.get('https://fbref.com/en/comps/9/Premier-League-Stats')
table = driver.find_element_by_id('div_stats_misc_squads')
table_html = table.get_attribute('innerHTML')
misc_df = read_html(table_html)[0]
misc_df.columns = misc_df.columns.get_level_values(1)
driver.close()
#Set path -- NEED TO CHANGE THIS TO YOURS!
path = '/Users/rachael.saxon/Documents/OneDrive - ans/Sample Datasets/FootballDataScraper/Notebooks/'
#Output to Excel
writer = pd.ExcelWriter(path+'FootballStats.xlsx', engine='xlsxwriter')
lt_df.to_excel(writer, sheet_name='LeagueTable', index=False)
homeaway_df.to_excel(writer, sheet_name='HomeAway', index=False)
squads_df.to_excel(writer, sheet_name='SquadStandardStats', index=False)
keeper_df.to_excel(writer, sheet_name='SquadGoalkeeping', index=False)
keeperadv_df.to_excel(writer, sheet_name='SquadAdvancedGoalkeeping', index=False)
shooting_df.to_excel(writer, sheet_name='SquadShooting', index=False)
passing_df.to_excel(writer, sheet_name='SquadPassing', index=False)
passingtypes_df.to_excel(writer, sheet_name='SquadPassingTypes', index=False)
gca_df.to_excel(writer, sheet_name='SquadGoalAndShotCreation', index=False)
defense_df.to_excel(writer, sheet_name='SquadDefensiveActions', index=False)
possession_df.to_excel(writer, sheet_name='SquadPossession', index=False)
playingtime_df.to_excel(writer, sheet_name='SquadPlayingTime', index=False)
misc_df.to_excel(writer, sheet_name='SquadMiscellaneousStats', index=False)
writer.save()