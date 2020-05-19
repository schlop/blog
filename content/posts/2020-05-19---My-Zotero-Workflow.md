---
title: My Zotero Workflow
date: "2020-05-19T00:36:11.388Z"
template: "post"
draft: false
slug: my-zotero-workflow
category: "Zotero"
tags:
  - "Zotero"
  - "Academia"
  - "References"
description: "Zotero is a reference manager that helps researchers to organize and keep track of academic papers. In this post, I will describe my workflow with Zotero, how I add papers to my library, how I manage and annotate them, and how I reference them in Word."
socialImage: "/media/zotero3.png"
--- 

[Zotero](https://www.zotero.org/) is a reference manager that helps researchers to organize and keep track of academic papers. In this post, I will describe my workflow with Zotero, how I add papers to my library, how I manage and annotate them, and how I reference them in Word.

During my Bachelors and Masters, I used EndNote to organize my papers. However, after starting my PhD and using EndNote almost every day, I became more and more annoyed by it. Performance was bad (adding a single reference to a word document took about 30s), the software architecture was old and unstable (32 bit), scripting was very limited, and I was missing some specific features to optimize my workflow (see below). So after a six months of suffering, I decided to switch to Zotero. The transition was really painful, because EndNote's abilities to export your library in a format that Zotero can read are very limited. But it was totally worth it and I'm really happy with my current setup.

## Adding papers to your Zotero Library

I use the official Chrome browser extension [Zotero Connector](https://chrome.google.com/webstore/detail/zotero-connector/ekhagklcjbdpajgpjgmbionohlpdbjgc) to add papers that I find online to my local Zotero library. I really like the simplicity of the extension: You click the extension button in your browser, an entry for the paper that you are currently looking at is created in your library, and if you have access to the PDF, it is downloaded as well and linked to the entry.

After I have added a paper to my library, I usually tag it. I am not very systematic when it comes to tags. My rule of thumb is to use not more than 2-3 tags and to stick with names that I have already used in the past. When a paper is specifically relevant for a certain project that I'm working on at the moment, I also add the paper to a Zotero group. Overall, I use labels more for the global organization of my papers and for an improved search, whereas I use groups for structuring references for a specific project/paper.

## Managing and annotating PDFs

Having 1000s of papers in your library is great, but a some point you have to eventually start reading them. When I am looking for something specific in a paper, and when I just want to quickly scan through it, I simply open the paper on my computer. However, when I want to study a paper in detail and read it from introduction to conclusion, I hate to it on a laptop. Before I was using Zotero, I just printed dozens of papers a week and annotated the hard copies with a pen. While I still love the physical interaction with the papers, this approach obviously has a couple of disadvantages: (1) Papers get lost quickly in an enormous stack on your desk, (2) they are only available at your office and (3), your ecological footprint suffers.

Therefore, I came up with a neat way to sync all PDFs in my Zotero Library via Dropbox with my iPad where I can read and annotate them with the Apple Pencil. To enable the workflow, just follow these steps.

1. Close Zotero
2. Navigate to your Zotero folder by typing the following command in your terminal `cd ~/Zotero`
3. Make a backup of your storage folder by typing `mv storage storage.backup`
4. Create a symbolic link that connects a Dropbox folder with the Zotero folder `ln -s ~/Dropbox/Zotero/storage ~/Zotero/storage`
5. Copy all files from the storage.backup folder into the new Zotero dropbox folder

This setup results in all papers being automatically uploaded to your dropbox. Unfortunately, the sub folders inside the storage folder are not named by authors. Therefore, it was tricky for me to open the PDF I was looking for on my iPad to annotate it. I solved this problem by using the App [Documents](https://apps.apple.com/us/app/documents-by-readdle/id364901807). In Documents I set up a synced dropbox folder (new files in the folder will be automatically downloaded to the iPad - nice!) in which I can then search for file names (despite using crude folder names, Zotero luckily names PDFs properly starting with the name of the paper's author(s).

![zotero2.png](/media/zotero2.jpeg)

So whenever I want to read and annotate a paper on my iPad, I just search for the author's name of the paper in Documents on my iPad, write my comments and close the file. After closing the file, it is automatically synced with my Dropbox again, and I can access the PDF with my handwritten notes in the Zotero library.

The only downside of the approach is that when you send a PDF to a colleague and do not want to share your annotations, you have to manually create a copy of your PDF in which you delete all annotations. I am planning to automate that in the future with a custom Python script. When I do, I will write about it on my blog.

An alternative to my annotation workflow is [Zotfile](http://zotfile.com/). It allows you to manually push papers to your tablet and later retrieve them from there. However, I don't like the push/pull mechanic and rather have my papers automatically synced.

## Quickly accessing and referencing papers in your Zotero library
One awesome piece of software that I use all the time to quickly access papers in my Zotero library is [Zothero](https://github.com/deanishe/zothero) for Alfred (a replacement for MacOS spotlight). After having installed Zothero, I can simply open Alfred, type `zot` and the author name, and I see all relevant papers in my search. Zotero does not even have to be running. This is super awesome when I talk to colleagues and just quickly want to show them this one really interesting paper on your computer.

![zotero3.png](/media/zotero3.png)

When I write a paper with Word, I use [Zotero's Word Plugin](https://www.zotero.org/support/word_processor_plugin_installation) to add references. So far, I have not used the Overleaf + Zotero combo, but I have that planned for this year. The integration process should be relatively straight forward, but I will keep you updated.

## Summary
I am using Zotero for almost a year now and I am super happy with it. In my opinion, Zotero is the best option when it comes to reference managers, but everyone should do their own research, because switching reference managers can be really painful.