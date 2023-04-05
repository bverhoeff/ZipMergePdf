This repository is just a handy method for an annoying problem that occurs when scanning large paper documents.

It so happens that my scanner jams after a number of pages when scanning larger two-sided documents. 

I solved this by scanning in two steps. First all front sides of the document are scanned to a PDF. Then all
back sides are scanned to a separate PDF. Now we have two PDF's, with odd and even pages and the even pages
are in reversed order. Merging these documents as is results in a very impractical PDF.

I couldn't find a tool that solved this easily for large documents but luckily ChatGPT helped me find pypdf.

The method in run.py handles the two PDF's and creates a zip-merged PDF with all pages in correct order.
And you don't need to leave credentials at 'free' online pdf websites. Tadaa....
