###This version depends on brew and ruby > 1.8.7.

It is a lazy thing to create debug messages where the content is less than informative, yet, I do this frequently. Rather than mashing my keyboard and achieving "asdawrf", or "hello", or "here", or any other number of non informative key presses, I now press F3 and generate a random string using succubus, a lovely ruby gem which I can hardly imagine a better use for!

Its evolved a bit and now there are a CSS and SASS versions which pull random, valid, color names.

I'm actually using them a lot, and I seem to be able to differentiate larger number of these random messages and colors, though I'm not sure this is a good thing, and I try to keep it to a minimum.

####Some sample <Debug Messages>:

 * Smarty black mamba
 * naughty gray fox
 * Red Privet hawkmoth
 * icy African Wild Dog
 * Orange Greenish Grass-dart frog
 * crazy honey bee
 * Green mallard

#### example use:

 *  *javascript*: console.log("Red honey bee", this);
 *  *Ruby* : puts "Smarty house mouse"
 
###Some sample <Sass Debug Color Mixins>:

 * @include debug(Aqua);
 * @include debug(LightBlue);
 * @include debug(DarkGray);
 * @include debug(MistyRose);
 * @include debug(Crimson);

####  example Sass Debug Mixin
@mixin debug($color){
  border:3px dotted $color;
}

### Some sample <Css Debug Color Borders>:

 * border: 2px dotted LemonChiffon !important;
 * border: 2px dotted Sienna !important;
 * border: 2px dotted LightYellow !important;
 * border: 2px dotted LavenderBlush !important;