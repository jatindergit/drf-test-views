# drf-test-views
If you're testing views directly using APIRequestFactory, the responses that are returned will not yet be rendered, as rendering of template responses is performed by Django's internal request-response cycle. In order to access response.content, you'll first need to render the response.
