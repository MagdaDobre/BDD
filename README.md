# BDD project
Behavior Driven Development(BDD) tests for websit: https://jules.app/sign-in

📝 
***_Theory_**:
 + BDD is an extension of Test Driven Development(TDD) where, instead of writing test cases, we start by writing a behavior
Later, we develop the code that is necessary for our application to perform the behavior.

The structure of a BDD framework is as follows:
1. Folder features = Feature files (files written in a more natural language (gherkin) to describe business scenarios)
    - Given (the context in which the action takes place)
    - When (the action we do)
    - Then (the check we want to do)
    
If we have steps that reproduce in several scenarios or in all, then we can put them in the Background (it's like the setUp in unittest)

2. Folder steps = Step definition files (technical mapping of business files - feature files)

3. Folder pages = Mapping pages for browser elements (POM - page object model)
     - We will have files for each page of the application
     - base_page file (we will have a class that contains methods that can be used in several classes, that is, which are useful for all pages)
     
4. Browser file (which will contain instructions for installing and opening the browser)

5. Environment file (which will contain the instantiation of all pages type classes)
