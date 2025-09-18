# Summary

The following document outlines how Brainbase implements custom integrations specifically for DGA. The document will outline the differences between Version 1 and Version 2 of the Brainbase platform, and the steps required for each. 


## Phase 1 - General Authentication and Tokens

This phase can take an hour (given correct scope and tokens) or longer if we have to reach back out to the provider to be granted tokens with different scope, different tokens for prod vs. sandbox, or need a sandbox account populated with correct data.

This can be an ongoing process, as sometimes issues with scope come up as you build out the integration. However, for the purposes of phase 1, follow the following steps.

Follow the following steps for this phase:

* Determine whether or not there is a sandbox and production environment. Sometimes, there will only be one environment. If there is a sandbox and production environment, ensure you gather both sets of keys. 
    * Sometimes, production keys will be blocked by the provider until we prove our application and go through an approval process. If this is the case, ensure you have the correct instructions/outline on how to acquire production keys once the sandbox is completed
* You will see a few options for authentication. 
    * Option 1 - Single API key to provide in the headers of api request. For this, you can skip the step
    * Oauth - most of the time, auth follows Oauth1.0, where you will have a set of tokens which you exchange for an expiring bearer token every X hours. If this is the case:
* Build out a function that returns a fresh token to be used in the headers of an api request
Find the simplest API endpoint you can and make a test request to it. Ensure you receive a 200 response. Once you achieve this, you are done with this step. 

## Phase 2 - Built out the integration

For this step, you will need to fill out the python file in this repo. You must ensure that the AI can achieve the following with **only** the functions defined in this python file. You can make multiple api calls within a single function, but you are limited to these function definitions.



