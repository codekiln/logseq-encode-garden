alias:: [[cmi5/AU]]
tags:: [[cmi5]], [[EdTech]], [[Standard]], [[Term]]

- # 🧩 cmi5 Assignable Unit (AU)
  - An AU is a discrete, launchable learning object—like a lesson, module, video, or simulation—that is:
    - assigned to a learner,
    - launched by the [[LMS]],
    - and reports results using [[xAPI]].
  - Think of an AU like a [[SCORM/SCO]], but designed to be:
    - More modern (works outside the browser),
    - Secure (uses xAPI tokens),
    - And decoupled from LMS constraints.
  - ## 🧱 Structure
    - In a typical cmi5 course:
      - The course has a manifest (`cmi5.xml`)
      - That manifest lists one or more AUs
      - Each AU includes:
        - A launch URL (or path)
        - Completion rules (`moveOn`)
        - Optional metadata (e.g., title, mastery score)
  - ## 🔁 Example
    - If a course has:
      - Module 1: "Intro to Data Privacy" (AU)
      - Module 2: "Case Study: GDPR Compliance" (AU)
    - Each AU can be launched independently, and each reports back learner progress and results via [[xAPI]].
  - ## Summary
    - AU = the atomic unit of learning in [[cmi5]], launchable and trackable via [[xAPI]].