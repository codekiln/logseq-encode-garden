description:: If you are outputting markdown, follow these rules
globs:: *.md

- # Rules to follow when outputting markdown
- It's important that there is only one level of triple-backtick fenced code blocks in markdown output.
- place your response in a triple-backtick fenced codeblock that's labeled with markdown, and use triple tilde fenced codeblocks for any inner code blocks, as per the CommonMark spec.
- <EXAMPLE>
- ```markdown
  Here's an example of the code: 
      ~~~bash
      $> git describe --tags
      ~~~
  ```
- </EXAMPLE>