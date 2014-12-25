Title: Analysing three months of academic spam
Date: 2013-08-30 05:42
Author: Peter
Category: Academic publishing
Slug: analysing-three-months-of-academic-spam

Can't get your paper in Nature? Publish it in the Journal of Ubiquitous
Computing and Applications, just pay the \$1000+ article processing fee,
they accept everything. Your paper was rejected from the leading
conference of your field? It had an acceptance rate of 0.5 % for the
past twenty years, do not be surprised. Why not try the International
Conference on Advanced Education Technology and Management Science? It
is not your field, but they accept anything if you pay the \$300
registration fee, and the proceedings will be indexed by the Whatever
Junk Compendex.

Academic buccaneers try to cash in on high rejection rates, frustration,
slow processing, and the high cost of open access publishing in renowned
journals. They spam my inbox indiscriminately, ignoring my subject area.
The calls for papers slip through the spam filters, no matter how much
effort I put into training those filters. I collected the academic spam
that arrived in my inbox between 2013-05-15 and 2013-08-30 to see what
kind of observations I can make.

Academic spam in numbers
========================

I received a total of 220 spam messages over the period, totalling 27
MBytes of wasted bandwidth. Out of the 27 MBytes, nearly 20 MBytes were
from the same sender, a repeated email by the considerate organizers of
the 3rd International Conference on Education and Education Management.
The next worst offender sent an email only tenth of the size.
Attachments otherwise were common, the most hilarious was when the
zealous organizers enclosed the author instructions in a doc file. About
71 % of the spam messages had the mail in HTML format.

  ---------------- ---------------------- --------------------
  **Total spam**   **Unique addresses**   **Unique domains**
  220              159                    77
  ---------------- ---------------------- --------------------

I processed the "From" field to extract the email address of the
senders. Looking at the domains where the mails were sent from, there
were only 77 of them (see the table above). The distribution was not
uniform, the majority of the mails came from 163.com, more precisely,
vip.163.com (see the figure below). The third worst offender was
vip.126.com. I am uncertain what grants a VIP status at these Chinese
providers, but if it is for money, then it apparently enables the VIP
address owners to spam indiscriminately. 188.com was also there, so not
surprisingly the majority of the spam included passages in Chinese.

[caption id="attachment\_514" align="aligncenter" width="549"]![Pie
chart of academic
spammers](http://peterwittek.com/wp-content/uploads/2013/08/academic_spammer_pie_chart.png)
Proportion of the domains of origin of academic spam.[/caption]

Google Mail came second, but this is misleading. Most of the Gmail
messages arrived from the obnoxious organizers of the 1st International
Conference on Advances in Computing, Communications and Informatics, in
Mysore, India. This conference was borderline legitimate, with Vinton
Cerf giving you the evil eye from the main website. Not all the blame
goes to the spamming-prone organizers: EDAS provided the platform to
send unsolicited calls in bulk. EDAS is a conference organizing tool. I
registered two years ago when IPDPS was using it. Unfortunately EDAS has
no respect for registered users, and allows seeking reviewers and
sending calls to any user who ever signed up, even if you explicitly
request not to. Moreover, it is not possible to delete an account. After
a few email exchanges, this is the best that I could extort from EDAS
tech support:

*If you prefer to receive no email, including no invitations to serve on
TPCs of any EDAS-managed conference, we can mark your email address as
invalid and you will not receive additional email.*

Since then, EDAS-related spam stopped, so I expect that spam from a
Gmail address will stop.

About 68 mails originated from senders who built a crawler good enough
to extract my name correctly. In four cases, they addressed my frequent
co-author instead, but with the accents in his name displayed
incorrectly. The others just started of with "Dear researchers", "Dear
colleagues" (oh my, no!), or just "Dear", followed by a comma. Wolter
Kluwer Health ambushed me with "Dear Medknow Member". I never wanted to
be a Medknow Member at the first place. Eighteen papers included an
apology for sending junk or potential cross-posting. A tiny fraction
included a link to unsubscribe, but I never dared to click on it. That
would be equivalent to writing a vexed reply to the usual "You inherited
a billion dollars" scam.

A better filter
===============

Filtering out any email that contains Chinese characters would solve
most of my problems, but I maintain good relations with the Tsinghua
University, and our correspondence frequently includes leftover Mandarin
from other emails. Other sophisticated, content-based filters failed, so
I need a simple, domain-based filter.

Since all my emails are in plain text format, they are easy to parse. An
approved domain list is equally easy to create once I see the unique
domain names. This script runs through my academic spam folder and
generates a new regexp that includes all spammy domains (the sed in the
third line should include a backslash before the parentheses, but it
would be parsed as an equation by WordPress, hence the backslashes were
stripped):

<div class="highlight">

    #!/bin/bash
    cat academic_spam/*|grep "^[Ff]rom: " | sed -e 's/[Ff]rom: //'|  
       sed -e 's/.*<(.*)>/\1/'|sed -e 's/ *//g'|sed -e 's/.*@//'|  
       sort|uniq > unique_domains.txt
    echo -n ".*@.*(" > spammers.txt
    grep -v -i -f approved.txt unique_domains.txt | tr '\n' '|' >> spammers.txt
    echo "dummyemailaddress)" >> spammers.txt
    rm unique_domains.txt

</div>

The current output is the following:

``` {.brush: .bash; .gutter: .false}
.*@.*(126.com|188.com|51email.org|AdvancesENG.com|academeresearchjournals.com|arpapress.com|aviabank.com|bkmeeting.org|charitylight.org|cloudcomcongress.com|conf-edu.org|conf-support.org|conferenceemail.com|config-ei.org|confmail.org|davidpublishing.com|dijon.inra.fr|e.enefmmail.org|ei-conf.org|ei-edu.org|fesb.hr|fzu.edu.cn|garjournals.org|geonf.org|hansqk.org|hrjoin.org|ica-itb.org|ieit-conf.org|ij-cm.org|ijnest.org|infotech2014.com|inhubei.org|iphsci.com|irjournals.org|journals.hindawi.com|ljemail.org|m-hikari.com|mail-conf.org|mail.2013iiisconferences.org|mail.vresp.com|medknow.com|meritresearchjournals.com|mililink.com|monmo.org|mst.edu|ncat.edu|newgroundresjournals.org|newworldpub.com|noreply100.com|noreply101.com|noreply106.com|omicsonline.net|plaan.org|pubpromotion.com|pubspress.com|pwr.edu.pl|robionetics.org|scientificadvancespublishers.com|scirp.biz|scirp.info|scirpinfo.org|scirpnews.org|sohu.com|solsbj-63.com|srpinfo.org|statisticalhorizons.com|sweeg.org|thesai.org|uav.ro|vip.126.com|vip.163.com|xiaolun.info|yaoyao-ei.org)
```

My domain uses CPanel, where user-level filtering allows using regexps.
I set that emails matching this pattern should make their way directly
to /dev/null. Waste of bandwidth is stopped at the server level.

Closing remarks
===============

Are all open access journals scams? No, but the ones you receive a call
from are. They are predatory publishers with fishy business models.
Pieta Eklund wrote a
[guide](http://bada.hb.se/bitstream/2320/11421/4/control_publisher.pdf "Open Access and predatory publishers")
how to identify the better ones, and Jeffrey Beall maintains a
[list](http://scholarlyoa.com/publishers/ "List of predatory publishers")
of predatory publishers. The situation is far bleaker with conferences,
and their calls make up the bulk of the spam. It is hardly enough that
the organizers discredit themselves by being associated with such
conferences. Most of these organizers are based in China, so it is also
hard to take legal action. Academia strives on open communication, but
your best line of defence is hiding your email address. I recently
removed my email from all freely available PDFs of my papers, except the
ones on arXiv, where no such changes are possible. This way at least an
automated crawler will be less likely to pick up my address. For the
spamming lists that already include me, the regexp generating script
should reduce their annoyance.

