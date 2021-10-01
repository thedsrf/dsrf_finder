
# CSS Selectors


 #### What do CSS Selectors do? How do they work?
 CSS is a web styling language used in most websites. By using CSS, you can select particular HTML elements from a webpage.
 #
 #### How to Write in CSS
 To use CSS, you need to understand some of the basics of HTML first. CSS selects elements based off of the tags and the attributes of those tags on the page.
 #
 #### Viewing a Page's HTML
 On any page, you can right-click and choose Inspect Element in ParseHub to view the HTML layout of the page. This is important to do, so that we can design CSS to pick out the element we want.

 Right-clicking on the particular element, if you can find it, and inspecting that element will take you to its tag's location in the HTML.

 If you hover over tags in the HTML view, the page will highlight the element that your cursor is hovering over. 
 
 
 ![demo pic](https://files.cdn.thinkific.com/file_uploads/456812/images/cbf/b2e/326/1619118281312.jpg?width=1920)
 #

 #### Selecting all elements

 To select all tags of one type, use: **tag**

 You should avoid typing this in for div or span tags because it can select many elements, causing library to crash. You should write your predicate first, something we'll learn about later.

 For example, to select all the links on the page, use **a**
 #
 #### Selecting all children
 HTML elements are nested, as you can see:

 ![demo pic](https://files.cdn.thinkific.com/file_uploads/456812/images/8f5/3d1/c9a/1619118298901.jpg?width=1920)

 Sometimes selecting every single kind of element isn't what we want to do, because we might only want links (a tags) that are in a particular section (like a div tag).

 We can write this: **div a**

 This translates to: "Select all **a** tags that are somewhere nested underneath **a div** tag." You can see here what would be selected, and what wouldn't be:

 ![demo pic](https://files.cdn.thinkific.com/file_uploads/456812/images/c9e/0a9/18f/1619118306545.jpg?width=1920)

 In red are the selected elements. Bolded is the first div that CSS recognizes they are nested under.
 #

 #### Filtering elements based on attributes

 We can use class selectors to narrow down our selection even further. For instance, we might only want to get all links that have a class attribute of "class". We can write this:

 **a.class**

 The period followed by text specifies a class of the tag being selected. The same thing can be done with # instead of . for id attributes. We can write:

 **a.anythingYouLike**

 This is a big jump because it can really let us pick out one element at a time, as long as each tag has a unique class.
 #

 #### Selecting elements by immediate children
 We've been using a space to select descendants so far, because the right arrow > has a special feature in CSS. It will only select children exactly one level down.

 In the code below, **div>a** will select only the highlighted immediate child of the div tag, but none of the **a** tags further down.

 #
 #### When the Tag Doesn't Matter
 Sometimes you just need to select an element based on the predicate and not the tag. This can come up if you need several tags of different types. You can use the symbol * instead of a tag to specify any element

 ***.other-products** will select the highlighted

 ![demo pic](https://files.cdn.thinkific.com/file_uploads/456812/images/f33/45d/a28/1619118348769.jpg?width=1920)

 
#
