# jupyter_autograder_2
A project to re-implement certain functions of nbgrader for jupyter notebooks.  

This project seeks to decouple the autograding aspects of jupyter's nbgrader extension from the necessity to have Kernels installed for the programming language being autograded.  The intended major features of this extension include the injection of arbitrary code into student answers (in order to establish preconditions and test postconditions), and the automation of certain reporting requirements for the accreditation of engineering programs in Ontario, Canada.  

So, you may be asking yourself, what about nbgrader is so bad that you felt you needed to do this?  It's not really about nbgrader, but the Kernels.  We recently had the experience in our course of finding out that the C kernel we were using misses the mark in a number of key areas.  The impetus here is to create an autograder that does not require a correctly installed jupyter kernel, just the ability to compile the files.  
