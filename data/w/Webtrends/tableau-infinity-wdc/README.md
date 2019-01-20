# tableau-infinity-wdc
[![Build Status](https://travis-ci.org/Webtrends/tableau-infinity-wdc.svg?branch=master)](https://travis-ci.org/Webtrends/tableau-infinity-wdc)

This page describes how to import an Infinity Report into Tableau by making use of the Tableau Infinity Web Data Connector (WDC) which was developed James Buckley, Peter Crossley and Evan Osherow.
 
[![Tableau](https://buy.tableau.com/images/logo.png)](http://www.tableau.com/)       [![Webtrends Infinity](https://www.webtrends.com/wp-content/uploads/2016/05/Infinity-Mark-Animated-DotCom11.gif)](https://www.webtrends.com/products-solutions/big-data-platform/)
 
#Intro - What can it do?
 
The Infinity WDC allows for reports made in Infinity to be hooked into Tableau.
It works by using the Infinity API, so it supports all current API capabilities.
It has a UI which builds out the API request within Tableau similar to how generator.webtrends.com built out the older Rest API.
Once within Tableau, the data can be refreshed automatically, allowing for dashboards/reports to easily integrate with Webtrends data.
 
##Step 1 - Producing the Data Export URL
 
     1. Open the report in Infinity that you wish to import into Tableau
     2. For "trends" reporting in Tableau, it helps to add a date/time dimension first (This is until the Infinity API can natively support trends reporting).
          
     3. Save the report if you need to.
     4. Once saved, click the "Exporting and Sharing" button located on the top right.
          
     5. Select JSON. (Technically the data type you select doesn't matter for the WDC, as it rebuilds the URL itself)
     6. Copy the generated URL.
          
 
 
##Step 2 - Entering the Data Export URL into the Infinity WDC in Tableau
 
     1. Open Tableau.
     2. Select the Web Data Connector option under the "Connect" side panel.
          
     3. Enter the following URL: https://webtrends.github.io/tableau-infinity-wdc/
     4. You should now see the Infinity WDC UI.
     5. Paste in the Data Export URL of the report.
          
 
     6. Some of the form fields should have been completed for you.
     7. Select the time range you want. Can be a relative range, or custom which displays calendar tools.
          
     8. Enter your Portfolio/Infinity credentials and click Connect.
     9. Tableau should begin loading the data.
 
 
##Step 3 - Configuring Webtrends Data in Tableau
 
     1. When the dimensions and measures have been successfully loaded, you'll see the option to "Update Now" and "Automatically Update"
     2. Click Update Now so we can first validate the collected data.

     4. You may see some dimensions with (null) in them, which we will remove later.
     3. If a Date field was added, change the file type of this column so Tableau recognizes it as a Date field. You'll need to update the data again afterwards.
          
     4. With the Data Source added, you can open a sheet to see the dimensions and measures available.
          
     5. To remove the (null) values, right click the affected dimensions and do the following:
          a. Create > Set
          b. Name the Set something appropriate like "Remove null values from Content Sub Group"
          c. Tick the "Null" checkbox
          d. Tick the "Exclude" checkbox
          e. Click OK
               
          f. Once the Set has been created, drag it into the Filters box.
               
     6. Now you can start dropping dimensions and measures into the sheet to create whatever chart/visualization you can think of.
     
