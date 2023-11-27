from zillow_scraper import ZillowScaper
from form_populator import FormPopulator


zillow = ZillowScaper()
zillow.getProperties()
property_list = zillow.property_list

form_populator = FormPopulator()
form_populator.open_form()

for property in property_list:
    form_populator.populate_form(property=property)
    form_populator.reload_form()
    
form_populator.self.driver.close()
form_populator.self.driver.quit()

