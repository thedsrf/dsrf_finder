# Xpath Selection
 
 In some cases, your target element is not visible on the page, and you might want to consider an alternative way to select elements on the page.  

 #### What does XPath do? How does it work?
 XPath is a language that lets you select particular HTML elements from a webpage.

 #### Why should I use XPath?
 In most cases, you shouldn't need to! However, there are a few cases where it might be necessary (or at least a lot more elegant) to use an XPath selection.
 This includes when you need data, such as latitutde and longitude, from a map where it isn't readily available hidden elements or previous data are being selected
 different pages on an eCommerce website have different page layouts
 
 You should try to use XPath selections when both Select Commands and CSS Selectors are not capable of selecting the elements you want. 
 
 #### How to Write in XPath
 To use XPath, you need to understand some of the basics of HTML first. XPath selects elements based off of the tags and the attributes of those tags on the page.

 This a refers to a link on the page, in an HTML <a> tag. The link itself is contained in the href attribute.
 
 ![pic demo](https://files.cdn.thinkific.com/file_uploads/456812/images/412/71a/dad/1619119542683.jpg?width=1920)
 
 You might have already noticed the href attribute mentioned if you use an Extract command on a selected link. XPath, however, doesn't extract elements, it only selects them. 
 
 #### Selecting all elements
 
 To select all tags of one type, use: **//tag**

 You should avoid typing this in for **div** or **span** tags, because it can select very many elements and cause ParseHub to crash. You should write your predicate first, something we'll learn about later.

 For example, to select all the links on the page, use **//a**

 #### Selecting all children
 HTML elements are nested, as you can see:
 
 ![pic demo](https://files.cdn.thinkific.com/file_uploads/456812/images/331/6a8/04c/1619119631881.jpg?width=1920)
 
 Sometimes, selecting every single kind of element isn't what we want to do because we might only want links (a tags) that are in a particular section (like a div tag).
 We can write this: **//div//a**

 This translates to: "Select all **a** tags that are somewhere nested underneath a table tag." You can see here what would be selected, and what wouldn't be:
 
 ![pic demo](https://files.cdn.thinkific.com/file_uploads/456812/images/e5d/446/9dd/1619119679755.jpg?width=1920)

  In red are the selected elements. Bolded is the first div that XPath recognizes they are nested under.
  
 #### Filtering elements based on attributes
 
 We can use predicate tags to narrow down our selection even further. For instance, we might only want to get all links that have a class attribute. We can write this:

 **//a[@class]**

 The @ followed by text specifies an attribute of the tag being selected.

 But, plenty of **a** tags have class attributes, what differentiates them is what the class attribute actually is! To do this, we can write:

 **//a[@class='anythingYouLike']**

 This is a big jump because it can really let us pick out one element at a time, as long as each tag has a unique class. When this isn't the case, you might have to look at another attribute, such as @id, or whatever else seems to distinguish it from other tags in the HTML.

 Sometimes, writing the exact phrase of the attribute can be slow and bulky. We can instead use contains

 **//a[contains(@class,'anythingY')]** will select all a tags that contain the phrase 'anythingY' in their class attribute, which effectively gets us the same thing as our previous selection. This can help, however, if tags have slightly different classes but share one particular part.
 
 ![demo pic](https://files.cdn.thinkific.com/file_uploads/456812/images/839/743/c33/1619119792422.jpg?width=1920)

 #### Filtering elements based on HTML structure
 
 Sometimes, we only need to select the first, second, or third element on page. We can use a number in predicate tags to specify which child, of the parent tag, to select. To select every 2nd link, we can write:

 **//a[2]**

 We can also combine this with our other predicates!

 **//img[contains(@class,'anythingY')][1]** will select the every image on the page which has the 'active' class first, under it's parent.

 Keep in mind that this **[#]** predicate is based on the parent, not the position on the entire page. In a layout like this:
 
 ![demo pic](https://files.cdn.thinkific.com/file_uploads/456812/images/004/676/a30/1619119940877.jpg?width=1920)

 **//a[1]** won't select the first link overall, but every link that comes first under its parent tag. You have to select the parents first, then use a [#] predicate tag, then select all first children.

 **//div[@class='row spacing-none']/div[1]//a[1]** is the XPath you need to select the first a tag link on the whole page.

 #### Selecting elements by immediate children
 
 We've been using a double slash so far, because the single slash / has a special feature in XPath. It will only select children exactly one level down.

 In the code below, **//div[2]/a** will select only the highlighted immediate child of the second **div** tag, but none of the **a** tags further down.
 
 ![demo pic](https://files.cdn.thinkific.com/file_uploads/456812/images/21d/faa/945/1619119988594.jpg?width=1920)

 You can, of course, combine predicates with these single slashes to get very specific selections with XPath.

 **//div[contains(@class,'spacing-nde')]/div[2]//img[contains(@class,'five-stars')]/a[1]** gets only the highlighted in the code below.

 #### When the Tag Doesn't Matter
 
 Sometimes you just need to select an element based on the predicate, and not the tag. This can come up if you need several tags of different types. You can use the symbol * instead of a tag to specify any element

 **//*[contains(@class,'other-products')]** will select the highlighted:
 ![demo pic](https://files.cdn.thinkific.com/file_uploads/456812/images/d3d/7c2/0ba/1619120047640.jpg?width=1920)

 Other times you'll want to check against the text actually shown by the tag. For this, you can use text(), such as in **//*[contains(text(),'Next Page')]**

 #### Logical Operators
 Finally, you can write **and** and **or** between predicates within square brackets if you need to use some even more specific tags.

 **//a[@aria-label='Stars' and contains(@class,'five')]**
 
 ![pic demo](https://files.cdn.thinkific.com/file_uploads/456812/images/746/1c4/bee/1619120105764.jpg?width=1920)
 
 You can also use not() in a predicate to rule out elements.

 **//div[not(contains(@class,'none'))]**
 
 ![pic demo](https://files.cdn.thinkific.com/file_uploads/456812/images/8c1/bc4/a51/1619120126549.jpg?width=1920)

