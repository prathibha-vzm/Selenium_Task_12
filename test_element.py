from selenium.webdriver.common.by import By

def test_parent_and_first_child(driver):
    #To locate the parent element of course
    href_parent=driver.find_element(By.XPATH,"//a[@href='/courses/']/parent::div[@class='⭐️rwl3jt-0 hidden lg:flex basis-auto']")

    #To get all the child elements under Parent
    child_elements=href_parent.find_elements(By.XPATH,'./*')

    #creating a list to store all the web elements
    child_text=[]

    #To Confirm the located element is Parent, printing all the child elements
    if child_elements:
         print("\n--Child Elements--")
         for elements in child_elements:
             print(elements.text)
             child_text.append(elements.text)

        #Storing the first element and second element
         first_child_index=child_text[0]
         second_child_index=child_text[1]

    #To locate the first child element
    first_child=driver.find_element(By.XPATH,"//div[@class='⭐️rwl3jt-0 hidden lg:flex basis-auto']/a")
    child_name=first_child.text

    #To print the located element **Confirmation**
    if child_name:
        print("\nFirst Child Name: ",child_name)

    assert child_name==first_child_index #assert the located element with stored first element

    #To find the second sibling
    second_sibling=driver.find_element(By.XPATH,"//a[@class='⭐️rwl3jt-0 my-2 cursor-pointer ml-2 mr-6 text-base font-normal text-gray-500 text-nowrap']/following-sibling::div")
    sibling_name=second_sibling.text

    #To print the located element  **Confirmation**
    if sibling_name:
        print("\nSecond-Sibling Name: ",sibling_name)

    assert sibling_name==second_child_index # assert the located element with stored second element


def test_all_elements(driver):
    #To find all the web elements under Courses
    all_siblings=driver.find_elements(By.XPATH,"//a[@class='⭐️rwl3jt-0 my-2 cursor-pointer ml-2 mr-6 text-base font-normal text-gray-500 text-nowrap']/following-sibling::*")
    print("\nSiblings of Courses")
    for name in all_siblings:
            print(name.text)

    #To Find all the preceding siblings of Products
    all_preceding_sibling=driver.find_elements(By.XPATH,"//div[@class='⭐️rwl3jt-0 group relative cursor-pointer mr-6 text-gray-500 hover:text-black'][3]/preceding-sibling::*")
    print("\nPreceding Siblings of Products")
    for name in all_preceding_sibling:
            print(name.text)

    #To Find all the ancestors of Parent element
    all_ancestors=driver.find_elements(By.XPATH,"//div[@class='⭐️rwl3jt-0 hidden lg:flex basis-auto']//ancestor::div")
    print("\nAll Ancestors of Parent Element")
    for name in all_ancestors:
        print(name.text)




