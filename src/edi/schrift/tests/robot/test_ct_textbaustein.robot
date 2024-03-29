# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.schrift -t test_textbaustein.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.schrift.testing.EDI_SCHRIFT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/schrift/tests/robot/test_textbaustein.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Textbaustein
  Given a logged-in site administrator
    and an add Schrift form
   When I type 'My Textbaustein' into the title field
    and I submit the form
   Then a Textbaustein with the title 'My Textbaustein' has been created

Scenario: As a site administrator I can view a Textbaustein
  Given a logged-in site administrator
    and a Textbaustein 'My Textbaustein'
   When I go to the Textbaustein view
   Then I can see the Textbaustein title 'My Textbaustein'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Schrift form
  Go To  ${PLONE_URL}/++add++Schrift

a Textbaustein 'My Textbaustein'
  Create content  type=Schrift  id=my-textbaustein  title=My Textbaustein

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Textbaustein view
  Go To  ${PLONE_URL}/my-textbaustein
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Textbaustein with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Textbaustein title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
