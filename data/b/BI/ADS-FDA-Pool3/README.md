# ADS-FDA-Pool3 under GS-35F-0538W
#README

* Prototype URL: http://dsoft-ads.cloudapp.net
* GitHub URL: https://github.com/DSoftTechnology/ADS-FDA-Pool3

The DSoft Technology ADS Pool 3 prototype and submission meets all the evidence criteria listed in Design Pool 3 and exercises/uses 7 (of 13) labor categories from the Full Stack Pool 3 categories.

##Full Stack Approach

DSoft Technology uses an Agile methodology (Scrum), an iterative, incremental framework for software project development. The team plans and monitors every two week interval using a tracking tool, our internally-developed AgileSprinter™, and projects are kept on track using frequent short standup meetings to communicate what has been accomplished and what roadblocks are preventing progress. A Scrum Master is assigned who is responsible for working with project managers to remove these roadblocks and to ensure the project stays on track.  At the beginning of the project, after writing a brief charter and requirements document, we develop use cases and add user stories and tasks to the product backlog for design, testing, and release documentation, with an estimated complexity and priority for each. Both backlog and requirements document are continually updated to keep up with evolving user requirements. Every two weeks, based on user priority, we pull user stories from the product backlog and add them to the current sprint. 

Screenshots provided under ...ADS-FDA-Pool3/Design/Sprint 1 Documents  

##U.S. Digital Services Playbook Evidence

###a) Assigned one leader and gave that person authority and responsibility

On June 17, 2015, K. Reece, Category 1 Product Manager, was assigned team leader, responsible and accountable for prototype delivery.  Ms. Reece has the skillset (PE, long time IT project manager and certified Scrum Master) to perform this role.  

Bio is located in ...ADS-FDA-Pool3 / Design / Meetings / 2015-06-17 / ProductManagerAppointment.md

###b) Assembled multidisciplinary and collaborative team

On 17 June 2015, team members were assigned to ADS prototype team under the following ADS labor categories and given time charging guidance/budget for Attach E submission:

| Name       | Category      |
| ---------- | ------------- |
| K. Reece   | Cat 1: Product Manager     |
| M. Coon    | Cat 2: Technical Architect |
| K. Lucas   | Cat 3: Interaction Designer/User Researcher/Usability Tester     |
| A. Brunner | Cat 4: Writer/Content Designer/Content Strategist     |
| M. Case    | Cat 5: Visual Designer     |
| T. Weckx   | Cat 6: Frontend Web Developer      |
| D. Hollenbach | Cat 12: Business Analyst    |

This assignment was documented in ...ADS-FDA-Pool3/Design/Meetings/2014-06-17/MeetingNotes.md

###c) Understand what people need

Entire project was conducted with human-centered design and tools focused on 3 users' needs (i.e., Financial Analyst, Business Owner, Food Recall Researcher).  Prototype meetings with users were conducted to ensure we understood what people needed.  Changes were continuously integrated, deployed on a staging system and tested, and then provided back to users for their reactions and additional inputs.

See ...ADS-FDA-Pool3/Design/Sprint 1 Documents

###d) Used at least 3 human-centered design techniques

Entire project conducted with human-centered design and tools.  Changes continuously integrated, deployed on a staging system and tested, then provided back to users for their reactions, criticisms and additional inputs.

* 1) Team brainstorming sessions - Worked within project team to brainstorm concepts and wireframes for development to meet user needs; developed user navigation map
* 2) Use Cases - 3 iterations centered on 3 identified primary personas (but not potential FDA data provider or maintainer personas)
* 3) Paper Prototyping - 3 iterations with 3 primary personas and using their comments to affect design
* 4) Participatory Design - Multiple live demonstrations (using both test data for quick reviews and FDA data once capability was integrated) showing prototypes to various users and incorporating their comments to inform/affect design
* 5) Usability Testing - Performed 1 iteration with uninvolved, non-technical users; invited non-IT users to use website and provide feedback to development team

###e) Created/used a design style guide or pattern library

See StyleGuide.md under ...ADS-FDA-Pool3/Design 

###f) Performed usability tests with people

* Put "needs of users first"
* Performed usability tests with non-technical and technical users
* See Usability Test Plan under ...ADS-FDA-Pool3/Design

###g) Used iterative approach

All 3 personas were involved in every iteration through general discussions, paper prototyping, app demonstrations and user testing.  

References:

* ...ADS-FDA-Pool3/Design/Meetings
* ...ADS-FDA-Pool3/Design/Sprint 1 Documents/Sprint1.md
* ...ADS-FDA-Pool3/Design/Sprint 2 Documents/Sprint2.md

An initial meeting with potential users uninvolved in design and development was held on June 18, 2015, and documented in /Design/Meetings/2015-06-18/MeetingNotes.md. In this meeting, users were assigned personas of: Food Recall Researcher, Financial Analyst and Business Owner. Initial ideas of what functionality would be useful for these personas was documented, and 3 use cases created.

Second paper prototype session was performed with customers on Monday, 22 June 2015, with DSoft’s Business Analyst and Visual Designer.  Customers/Personas identified changes and added requirements to the web forms and resultant reports (generated from open.FDA.gov).  Changes were made to use cases to capture changes, separate variants of use case. Some requirements were deferred until next build.

Third paper prototyping session was held with the Financial Analyst because we determined FDA dataset was limited and may not be able to provide exact report originally requested.

Live demonstrations of prototypes were provided to users whose comments/criticisms were reflected into design when possible.

###h) Created a prototype that works with multiple devices
Developed prototype to be responsive and successfully tested on various mobile and traditional devices including iPad, Android phone, iPhone, ChromeBook, PCs.

Multiple devices documented in ...ADS-FDA-Pool3/tree/master/Test

###i) Used at least 5 modern and open source technologies

The following were used in design and development of ADS prototype:
* Mono (http://www.mono-project.com)
* D3.js (BSD license) (http://d3js.org)
* JSON.Net (MIT license) (http://www.newtonsoft.com/json)
* Bootstrap (MIT license) (http://getbootstrap.com)
* ASP.Net MVC5 (Apache 2.0 license) (http://www.asp.net/open-source)
* TopoJSON (https://github.com/mbostock/topojson)
* NUnit (http://www.nunit.org/)
* Postal (https://github.com/andrewdavey/postal)
* PagedList.Mvc (https://www.nuget.org/packages/PagedList.Mvc)
* nginx (http://nginx.org)
* Debian Linux (https://www.debian.org/)
* Docker (https://www.docker.com)

###j) Deployed the prototype on IaaS or Paas

Deployed ADS prototype on Microsoft Azure, an IaaS / PaaS provider

Documented in ...ADS-FDA-Pool3 / Design / PaaS_Hosting.md 

###k) Wrote unit tests for code

* Created automated tests to verify all user-facing functionality
* Test Plan finalized on 25 June 2015
* Testing team session planned for Friday, 26 June 2015 using multiple mobile devices and various operating systems with users unfamiliar with system and development
* All web forms tested for compatibility on major browsers

Tests documented in ...ADS-FDA-Pool3/tree/master/Test

###l) Used Continuous Integration System to automate tests and continuous deployed to IaaS / PaaS provider

We deployed ADS protype to Debian Linux VM on Microsoft Azure, an Iaas / PaaS provider.  ADS prototype deployment is fully automated using TeamCity. Commits pushed to Github trigger a TeamCity build process which will pull the latest code, install / update dependencies (NuGet packages), run NUnit and code coverage. If all build steps are successful, build artifacts are packaged as a Docker image and deployed onto staging Linux host for QA / Integration tests. After success in QA, the automated deployment to Azure Production Linux host is triggered in TeamCity.

Documented in ADS-FDA-Pool3 / Deployment.md 

###m) Used Configuration Management

* Github (Source Control) - Used Github's built-in configuration management and control capabilities to ensure all documentation and artifacts were versioned, branched and committed with all changes; all software versions were committed and  TeamCity build process pulled latest code from Github, installed / updated dependencies (NuGet packages), ran NUnit tests and performed code coverage assessment.

* TeamCity (Continuous Integration) - all builds versioned and tagged.

###n) Used Continuous Monitoring

Azure VM PaaS comes with built-in continuous monitoring of CPU, Memory, Bandwidth, HTTP errors, Response times, Page Requests. Alerts can be configured as well as automatic scaling of underlying infrastructure based on metrics.  Reference Web Apps Dashboard here: 
https://azure.microsoft.com/en-us/documentation/articles/web-sites-monitor/

In addition, used New Relic (http://newrelic.com) to monitor utilization and performance on both Linux VM and Docker containers.  Both Azure and New Relic provide customizable reports and alerts which provide continuous data to the Ops team. The Ops team has procedures in place for responding to any event which is outside normal operating parameters.

###o) Deploy software in a container

Deployed solution in container using Docker.  Docker is an open-source project that automates deployment of applications inside software containers by providing an additional layer of abstraction and automation of operating-system-level virtualization on Linux.

###p) Install and run prototype on another machine

The included Docker file can be used to recreate Docker image from source code and deploy to any Linux OS that supports Docker hosting. For development purposes, source code can simply be opened with MonoDevelop or Xamarin Studio and run using the built-in XSP webserver.

Reference: ...ADS-FDA-Pool3 / docker / 

###q) Prototype and underlying platforms used to create and run prototype are openly licensed and free of charge

DSoft Technology developed the prototype in Mono v4.0.3 (an open source development platform based on the .Net framework) using Xamarin Studio (free open-source IDE) and the open-source tools listed in Section (i) above. Nginx and FastCGI Mono Server where used inside a Docker container using a Debian Linux VM on Azure PaaS for hosting.
