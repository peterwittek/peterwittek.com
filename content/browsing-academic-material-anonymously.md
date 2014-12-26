Title: Alarming state of browsing academic material anonymously
Date: 2014-09-03 03:35
Author: Peter
Category: Academic publishing
Tags: Academic publishing, Espionage
Slug: browsing-academic-material-anonymously
Summary: Cookies, browser-fingerprinting, tracking, and blocking of Tor exit nodes are becoming standard strategies while reading abstracts and exporting citations.

Academic publications sit behind pay-walls, and to access papers, you
need an approved IP address of your university, log in to your library,
or pay online per article. One way or the other, you will be identified.
Far more alarming is that even browsing through abstracts and obtaining
citations are losing the option of anonymity. Some publishers require
cookies to use their sites, others make Javascript mandatory to just
export a citation, and, more recently, Tor exit nodes are being blocked.
Academic publishers want your money and every last bit of data of your
life.

In the following, I describe the results of a brief experiment with the
publishers whose publications I access most often. The publishers in the
test were Elsevier, Springer, Wiley, Taylor & Francis, World Scientific
(WS), IEEE, ACM, American Physical Society (APS), SIAM, Royal Society
Publishing, Nature Publishing Group (NPG), Science/AAAS, and Proceedings
of the National Academy of Sciences (PNAS). I also included Google
Scholar (GS), as unfortunately I use it frequently for finding
citations.

Three IP addresses were used in different browser sessions: one ordinary
address in Tokyo, one university IP address in Sweden, and a Tor exit
node. I used a plain Firefox 32 under Linux with the non-Tor IP
addresses, with the user agent manually set to "Mozilla/5.0 (Windows NT
6.1; rv:24.0) Gecko/20100101 Firefox/24.0". The Tor Browser Bundle was
version 3.6.4, the user agent string matched the other two browser
sessions. All plugins were disabled, and all browser were fitted with
[NoScript](http://noscript.net/),
[HTTPS-Everywhere](https://www.eff.org/https-everywhere), and
[Disconnect](https://disconnect.me/). The cookie and Javascript settings
were modified, as the experiments required. When Javascript was enabled,
it was temporarily enabled for the entire page. Third-party cookies were
never enabled.

The purpose was not to access papers: only to obtain information about
the papers. Hence I tested two functionalities: accessing the abstract
page and exporting the citation to Bibtex. The procedure was to search
for the title of a paper published by one of the listed publishers with
[Startpage](https://startpage.com/). A click from there would take me to
the abstract page. From there, I tried exporting the citation. With
Google Scholar, the search took place in Google Scholar itself.

The Japanese and the Swedish IP addresses did not make a difference in
the outcome, hence the two cases are not separated. The blocking of Tor
exit nodes is inconsistent, hence the results may not be easy to
reproduce. In any case, if Tor worked, exporting the Bibtex citation was
also possible. The results are summarized in the following table.

|            | **Abstract**                       |||**Bibtex**  ||
|------------|------------|------------|------------|------------|------------
|            | **Cookies**|**Javascript**|**Tor**   |**Cookies** |**Javascript**
|**Elsevier**| No         |  Required  |    Blocked |    No      |   Required
|**Springer**| No         |  No        |   Yes      |    No      |     No
**Wiley**  |  No  |    |     No  |         Yes  |        No      |     No
**T&F**  |    Required  |   No  |         Yes  |        Required  |   No
**WS**  |     Required  |   No  |         Yes  |        Required  |   Required
**IEEE**  |   No  |    |     No  |         Yes  |        Required  |   Required
**ACM**  |    No  |    |     No  |         Blocked      No  |         No
**APS**  |    No  |    |     No  |         Yes  |        No  |         No
**SIAM**  |   Required  |   No  |        Yes  |        Required  |   No
**RSP**  |    No  |    |     No  |         Blocked      No  |         No
**NPG**  |    No  |    |     No  |         Yes  |        N/A  |        N/A
**AAAS**  |   No  |    |     No  |         Yes  |        No  |         No
**PNAS**  |   No  |    |     No  |         Yes  |        No  |         No
**GS**  |     No  |    |     No  |         Blocked  |    No  |         Required

Taylor & Francis requires cookies. A
[warning](http://www.tandfonline.com/action/cookieAbsent) comes up if
cookies are disabled, blocking you from further access. Among other
nonsense, it says "To provide access without cookies would require the
site to create a new session for every page you visit, which slows the
system down to an unacceptable level." SIAM and World Scientific will
tell you the exact same message.

The Javascript and the corresponding browser-fingerprinting fare worse.
IEEE Xplore pretends you can export a citation without Javascript, but
actually you cannot. IEEE wants both cookies and Javascript, and, as a
matter of fact, it also requires access to addthis.com, only to export a
citation. World Scientific also requires both cookies and Javascript for
exporting Bibtex.

ScienceDirect makes extensive use of Javascript and accesses third-party
sites, including many invasive trackers. Here is one more entertaining
morsel of information of Elsevier's IT infrastructure: book manuscripts
are uploaded through an unencrypted http interface. That is right, even
the password goes out in the wild, without encryption. When I complained
about it, the response was that the submission system was safe. Later I
was provided an FTP access to address my complaints. I was
flabbergasted. They spend serious money on stealing data from you
through ScienceDirect, but they are incapable of moving the submission
system to https. This is how much they care.

Not all Tor exit nodes are blocked systematically yet. I noticed that
from certain exit nodes, Royal Society Publishing and ScienceDirect are
blocked: the pages would not load. I imagine attacks are frequent from
Tor exit nodes, and they choose the most brainless form of defence:
block the IP address. Their profits are obviously not channelled towards
hiring competent IT personnel. I am not surprised to see ACM on the list
of blockers: they are sponsored by the
[NSA]({filename}/full-page-ad-by-nsa-in-the-communications-of-the-acm.md "Full-page ad by NSA in the Communications of the ACM"),
they glorify the actions of the NSA by calling the employees
\`[law-abiding dedicated
patriots](http://cacm.acm.org/magazines/2014/5/174340-the-nsa-and-snowden/fulltext "Law-abiding dedicated patriots")'
in their flagship publication, their new spam filter is even more
closely tied to Google, and they recently added tracking links to their
newsletters. Blocking Tor exit nodes to access the digital library is
the least they can do.

Going beyond publishers, searching for articles is also getting more
painful. Google blocks searches from Tor exit nodes, that is nothing
new. What is new is that Google Scholar updated its user interface a few
days back. I relied on a trick to get the Bibtex reference for a paper
without enabling Javascript: if any of the authors of the paper had a
Google Scholar profile, finding the paper on the profile page allowed a
Javascript-free export of the citation. This is gone. Now Javascript is
mandatory even to look beyond the first page of papers on a profile.
Also, there is no simple way to disable localization -- adding &hl=en to
every URL is cumbersome. I speak neither Japanese nor Swedish, so using
Google Scholar is a permanent pain. Can we just assume that academics
who managed to get a PhD one way or the other can speak elementary
English? Then we could forget about this localization madness. Reasons
are getting stronger and stronger to abandon Google Scholar, but the
alternatives still have serious shortcomings.

The most hilarious finding of this experiment is that Nature only
exports citation to RIS format. It must be hard to provide a Bibtex
option.

We all know that academic publishers are
[evil](http://www.theguardian.com/commentisfree/2011/aug/29/academic-publishers-murdoch-socialist).
Until now, they only wanted to cash in. They are going a step further
and they are ramping up efforts to harvest data about you. For what? I
prefer not knowing. Most of the major publishers are either based in
Five Eyes countries, or have extensive operations there. Espionage is in
their blood. The state of affairs is depressing as it is, and the
situation is only getting worse.

