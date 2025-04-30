alias:: [[IMS Content Packaging XML]]
tags:: [[IMS]], [[EdTech]], [[Standard]], [[XML]], [[Content Packaging]]

- # IMS Content Packaging
  - ## 📦 Overview
    - **IMS Content Packaging** is a standard developed by 1EdTech (formerly IMS Global) for structuring and exchanging digital learning content between systems. It defines how to organize and describe a collection of learning resources (e.g., HTML pages, quizzes, multimedia) into a single, transportable unit—commonly a [[Compression/zip]] file—so that it can be imported/exported across compatible Learning Management Systems ([[LMS]]).
  - ## 📁 Core Concept
    - An IMS Content Package includes:
      - A **manifest file** (`imsmanifest.xml`) describing the structure, order, and metadata of the content.
      - One or more **resources** (e.g., HTML, video, PDFs, SCORM modules).
      - Optional metadata and sequencing instructions.
  - ## 🗂️ Key Components
    - **imsmanifest.xml**: The required root file in every package. It defines:
      - `<organizations>`: the hierarchical structure of the course (modules, items).
      - `<resources>`: links to actual content files.
      - `<metadata>`: optional descriptive metadata about the course or items.
    - **resources/**: Folder containing the actual learning content (HTML files, images, documents, etc.).
    - **schemas/** *(optional)*: Definitions of custom XML schemas used in the manifest.
  - ## 🧠 Features
    - **Platform-neutral content structure**
    - **Supports metadata tagging** using standards like [[IEEE/LOM]] or [[Dublin Core]]
    - **Defines hierarchical relationships** among learning units
    - **Flexible**: Can encapsulate a simple lesson or a complex multi-module course
    - **Supports reusable content objects**
  - ## 📤 Use Cases
    - Exporting a course from one LMS and importing it into another (e.g., [[Canvas]] → [[Moodle]])
    - Packaging [[EdTech/OER]] content for distribution (Open Educational Resources)
    - Structuring multi-format learning resources for institutional archiving or sharing
    - Integrating assessments defined in [[IMS/QTI]] (Question and Test Interoperability)
  - ## 🔄 Related Standards
    - [[IMS/Common Cartridge]]: A profile of IMS Content Packaging with tighter constraints and added features like QTI and LTI links.
    - [[SCORM]]: Uses IMS Content Packaging as its packaging layer but adds runtime behavior and tracking.
    - [[cmi5]]: Uses a simpler manifest model and [[xAPI]] for tracking; not built on IMS CP.
  - ## 🧪 Example `imsmanifest.xml` Skeleton
    - ```xml
      <manifest identifier="course123" xmlns="http://www.imsglobal.org/xsd/imscp_v1p1">
      <metadata>
        <schema>IMS Content</schema>
        <schemaversion>1.1.4</schemaversion>
      </metadata>
      <organizations default="org1">
        <organization identifier="org1">
          <title>Sample Course</title>
          <item identifier="item1" identifierref="res1">
            <title>Lesson 1</title>
          </item>
        </organization>
      </organizations>
      <resources>
        <resource identifier="res1" type="webcontent" href="lesson1.html">
          <file href="lesson1.html"/>
        </resource>
      </resources>
      </manifest>
      ```
  - ## ✅ Advantages
    - Interoperability across systems
    - Backed by an open standard (1EdTech)
    - Widely adopted in education and training systems
    - Supports legacy and modern LMSs
  - ## ⚠️ Limitations
    - Does not define runtime behavior (e.g., scoring, completion)
    - Sequencing support is minimal compared to SCORM 2004
    - Verbose XML can be difficult to hand-author
    - Limited support for complex interactivity (requires linking to external tools like [[LTI]])