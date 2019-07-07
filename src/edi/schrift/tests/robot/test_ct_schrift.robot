# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.schrift -t test_schrift.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.schrift.testing.EDI_SCHRIFT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/schrift/tests/robot/test_schrift.robot
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

Scenario: As a site administrator I can add a Schrift
  Given a logged-in site administrator
    and an add Schrift form
   When I type 'My Schrift' into the title field
    and I submit the form
   Then a Schrift with the title 'My Schrift' has been created

Scenario: As a site administrator I can view a Schrift
  Given a logged-in site administrator
    and a Schrift 'My Schrift'
   When I go to the Schrift view
   Then I can see the Schrift title 'My Schrift'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Schrift form
  Go To  ${PLONE_URL}/++add++Schrift

a Schrift 'My Schrift'
  Create content  type=Schrift  id=my-schrift  title=My Schrift

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Schrift view
  Go To  ${PLONE_URL}/my-schrift
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Schrift with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Schrift title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
