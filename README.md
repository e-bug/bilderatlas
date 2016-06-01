# bilderatlas
Repository for 'Bilderatlas' project in Digital Humanities at EPFL, 2016.<br />
_E.Bugliarello, E.Caputo, A.Giunto_
<hr />

<p style="text-align: justify;">This work takes inspiration from a common situation. Imagine you are walking in a corridor of a museum, and you get stuck in front of a painting, thinking that you have already seen it somewhere. However, as human beings, we cannot remember all the paintings we have seen in our life. It is here that modern tools could come into play and help us.</p>

<h2 style="text-align: justify;">Definition</h2>
<p style="text-align: justify;">Bilderatlas is a collection of tables, made by Aby Warburg, based on fourteen different themes. Warburg was a German art historian who, in the last two years of his life, started working on this atlas. His work, however, remained incomplete [1].</p>
<p style="text-align: justify;">For each table, he pinned on a wooden panel several pictures and paintings that share a common theme. Even with a vast knowledge on the subject, the amount of artworks he considered is very small compared to today’s available databases of images. So, by implementing his wide knowledge with computing power, what could have Warburg done using modern tools?</p>
<p style="text-align: justify;">The aim of our project is to find an answer to this question. We try to create a sort of continuation to his work and to explore patterns in the tables with the help of today’s technologies.</p>

<h2 style="text-align: justify;">Setup</h2>
<p style="text-align: justify;">We chose some tables from the Bilderatlas in which images have strong visual similarities, and some where a pattern is not markedly evident. The four chosen tables are here reported, with a brief explanation on why we selected them:</p>

<ul style="text-align: justify;">
 	<li><strong>Table 2</strong>. It is rather a conceptual table, with little or no visual similarity among the paintings. <a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/03/atlas_2_nera_mini.jpg"><img class="size-medium wp-image-5428" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/03/atlas_2_nera_mini-233x300.jpg" alt="Table 2 - Greece as home of anthropomorphic representation of the cosmos, with mythological figures crowding the sky. [3,4,5]" width="233" height="300" /></a> <br />_Table 2 - Greece as home of anthropomorphic representation of the cosmos, with mythological figures crowding the sky._ [3,4,5]</li><br/>
 	<li><strong>Table 45</strong>. This table contains several paintings of buildings that have a similar internal architecture, with scenes in the foreground. The theme of the table sees dynamic, violent scenes, in contrast with calm, static scenes.<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/03/atlas_45_nera_mini.jpg"><img class="size-medium wp-image-5426" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/03/atlas_45_nera_mini-231x300.jpg" alt="Table 45 - Lethal threats (e.g., tyranny, war) against the possibility of achieving psychological “balance”. [3,4,5] " width="231" height="300" /></a> <br />_Table 45 - Lethal threats (e.g., tyranny, war) against the possibility of achieving psychological “balance”. [3,4,5]_</li><br/>
 	<li><strong>Table 46</strong>. The theme of the <em>Nymph</em> can clearly be observed by the human eye in several of these paintings, but it is interesting to see whether the CNN is able to recognize the figure starting from the woman in the <em>La nascita di San Giovanni Battista</em> by Domenico Ghirlandaio (top, right in the image below). <br /><a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/03/atlas_46_nera_mini.jpg"><img class="size-medium wp-image-5427" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/03/atlas_46_nera_mini-237x300.jpg" alt="Table 46 - Series of variations on Ghirlandaio's fruit-bearing “nymph”, reported in paintings, drawings and photos. [3,4,5]" width="237" height="300" /></a> <br />_Table 46 - Series of variations on Ghirlandaio's fruit-bearing “nymph”, reported in paintings, drawings and photos. [3,4,5]_</li><br/>
 	<li><strong>Table 25</strong>. It is a strictly visual table with <em>stone and pillar reliefs</em>.<br /><a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/03/T25_HD.jpg"><img class="size-medium wp-image-5424" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/03/T25_HD-249x300.jpg" alt="Table 25 -The harmonic structure of the Apollonian cosmos and the Dionysiac dynamism of the goddesses. [3,4,5]" width="249" height="300" /><br /></a> _Table 25 - The harmonic structure of the Apollonian cosmos and the Dionysiac dynamism of the goddesses. [3,4,5]_</li><br/>
<h2 style="text-align: justify;">Methodology</h2>
<p style="text-align: justify;">In some tables there is no apparent pattern connection among images, and visual patterns are difficult to discern. As a consequence, it is more difficult to relate pictures in the same table to their theme by using computational methods based on visual features. In any case, we are not interested in being able to find the same images that Warburg connected in a certain table; our aim is rather to continue his work on a large database of images.</p>
<p style="text-align: justify;">Since we are dealing with pictures connected by patterns that are not strictly visual, we need to use a research method based on a high-level representation of the images. This means that the pictures must not be read just as a collection of pixels, but rather in a more informative way. Therefore, we base our analysis on deep learning techniques. In particular, Convolutional Neural Networks (CNNs) seem to be the most appropriate choice in approaching this task [2].</p>
<p style="text-align: justify;">A neural network is a model that tries to emulate the human brain and its way of processing. In the image-processing context, the algorithm takes as input an image and extracts a feature array that characterizes it. The array will be a high-level representation of the image, which will thus allow to recognize patterns that are not strictly visual.</p>

<h2 style="text-align: justify;">Analysis</h2>
<p style="text-align: justify;">To launch the queries, we use DH Replica, a web server developed at the DH Lab that allows to perform CNN analysis on a database of more than 40,000 images (still a small database compared to today’s possibilities). Thanks to DH Replica, we can easily select multiple images in the database and launch a query, visualizing directly the result (Figure 1).</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/04/PP3_Fig1.png"><img class=" wp-image-5705" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/04/PP3_Fig1-300x225.png" alt="Figure 1 - DH Replica server" width="563" height="422" /></a>  <br />_Figure 1 - DH Replica server._
<p style="text-align: justify;">In the DH Replica, the images can be set to positive, which means that the pattern we are looking for is present in the image, or to negative, which obviously implies that the pattern is not present. However, at the time of our project, the research with negative images did not produce reasonable results. We thus performed queries with positive images only.</p>
<p style="text-align: justify;">As we will see below, the strength of this research comes from the computation of a common pattern when launching multiple images; the CNNs are often able to extract the pattern and find it in the database. For instance, when launching a single image, the desired pattern can be strengthened by performing a new query together with an image in the results that shows the pattern we are searching for.</p>
<p style="text-align: justify;">We have also written a bot whose role is to launch queries. It can accomplish the same tasks as the DH Replica. However, since the latter considerably simplifies the visualization of the results, the purpose of this bot is mainly to receive the scores for the query, together with the annotations relative to the images, thus allowing a deeper analysis.</p>

<h2 style="text-align: justify;">Results</h2>
<p style="text-align: justify;">As far as visual similarities are concerned, the CNN algorithm used by DH Replica works well. We also had some interesting results concerning more complex patterns. We present now a few of the queries that we have performed, focusing on the more surprising results.</p>

<h3 style="text-align: justify;"><strong>Table 25: </strong>Figures in movement and frame pattern</h3>
<p style="text-align: justify;">Among the different themes represented in table 25, we have the Muses. It is interesting to note that this theme is also present in table 2. However, here, they are part of the more global pattern representing figures in movement.</p>
<p style="text-align: justify;">The CNNs were able to find the pattern of the figures in motion (Figure 2). In fact, if we query <em>Apollon,</em> and <em>Angels Playing a Lute and Tambourine</em>, we obtain different sculptures showing people in non-static positions.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/1.jpg"><img class="wp-image-6160" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/1-300x81.jpg" width="578" height="156" /></a> <br />_Figure 2 - Query of Apollon and Angels Playing a Lute and Tambourine. Images in the red box are the queried images._
<p style="text-align: justify;">This is a very impressive result for the CNN algorithm. It could capture the transitory movements of hair and garments present in these reliefs, which is a non-trivial pattern that is investigated in today’s research studies.</p>
<p style="text-align: justify;">If we only query <em>Apollon</em>, by Agostino Di Duccio, which is a relief representing him between two columns, we obtain as results other sculptures contained in a frame. Not only do we have figures between two columns, but also other statues contained in square boxes, in some cases topped with an arch. This means that the CNN algorithm, given this relief, extrapolated the <em>frame</em> feature (Figure 3).</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/2.jpg"><img class="wp-image-6174" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/2-300x73.jpg" alt="Apollon" width="608" height="148" /></a> <br />_Figure 3 - Query of Apollon, table 25._
<p style="text-align: justify;">By adding <em>The Moon</em>, another relief by Agostino Di Duccio, we can confine our research to the <em>column</em> pattern, another main visual theme in this table (Figure 4).</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/3-1.jpg"><img class="wp-image-6177" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/3-1-300x73.jpg" width="600" height="146" /></a><br />_Figure 4 - Apollon and The Moon, Di Duccio._
<p style="text-align: justify;">In particular, among the returned artworks, we notice <em>St Peter</em> of Michelangelo, which contains the same column style as in <em>Apollon</em> and <em>The Moon</em>. This is a very interesting outcome since it shows how a given pattern might be repeated in different centuries (fifteenth and sixteenth centuries, respectively).</p>
<p style="text-align: justify;">This table also contains some pictures of temples with arches in their façades (in particular, the Malatestian Temple, shown in figure 5), representing the theme of power, which is recurrent in the entire Bilderatlas collection.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/40.png"><img class="wp-image-6178" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/40-300x134.png" alt="templeMalatesta" width="387" height="173" /></a> <br />_Figure 5 - Malatestian Temple, table 25._
<h3 style="text-align: justify;"><strong>The power of feature extraction from multiple images</strong></h3>
<p style="text-align: justify;">In Figure 6 we report the images from table 2 that we have used for our queries.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Table2.png"><img class=" wp-image-6103" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Table2-300x87.png" alt="Figure BOH - Images from table 2" width="569" height="165" /></a> <br />_Figure 6 - Images from table 2. Letters refer to the position of the image inside the table. Taken from [5]._
<p style="text-align: justify;">An interesting query is that of miniatures in table 2. By searching for the four miniatures (7a, 7c, 7d, 7f), the CNNs find several other miniatures, although inserting (quite low in the rankings) some paintings that are not actually miniatures (Figure 7). It is interesting to point out how the CNN recognized the drawing on paper, which is the only common feature among the found miniatures. However, when launching one single miniature, only one of the other four is found. This is due to the importance of the background, as the background of 7c is similar to 7d’s, while 7a’s is similar to 7f’s. Not very many miniatures are found by launching one single miniature, meaning that the CNN needs to compute a common feature (obtained only through multiple images) to find other miniatures.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/miniatures.png"><img class=" wp-image-6105" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/miniatures-300x197.png" alt="Figure BOH - Results of the miniatures query. Images in red box are the queried images." width="729" height="479" /></a> <br />_Figure 7 - Results of the miniatures query._
<p style="text-align: justify;">From table 46, if we launch the miniature <em>Book of Hours of Étienne Chevalier: Birth of John Baptist</em> by Fouquet (Figure 8) we also get a few miniatures. However, their style is totally different from the miniatures found in table 2. In this query we see the dominance of blue and red colors, which appear in the first results. We have a taste of how important the colors are when the CNNs compute the characterization vector of the images.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Fouquet.png"><img class=" wp-image-6106" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Fouquet-268x300.png" alt="Figure BOH - Query of Fouquet's miniature, from table 46." width="626" height="701" /></a><br />_Figure 8 - Query of Fouquet's miniature, from table 46._
<p style="text-align: justify;">An additional example of strong visual pattern is that of <em>Madonna with the Child</em>, by Fra Filippo Lippi (Figure 9). When launching this query, we astonishingly get a series of results with women with children on their laps, in several positions (Figure 9). We observe that the sixth score reported an image that has nothing to do with the pattern we are searching for. To get rid of this result, we just need to strengthen the pattern by adding another image to the initial query, for example <em>Madonna with the Child and two angels</em> and the other detail from<em> Madonna with The Child</em> of Filippo Lippi (Figure 9). In this case, the undesired painting has a much lower score (we find it at the twentieth position). It is interesting to notice that in the first paintings with closest scores, the child arms are raised, just like in the queried painting (in lower scores we do not necessarily see this feature).</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Lippi_TOT-1.png"><img class=" wp-image-6110" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Lippi_TOT-1-300x161.png" alt="Figure BOH - Query of Madonna with the child, by Fra Filippo Lippi, table 46. We observe how by strengthening the pattern we can get rid of undesired results." width="725" height="389" /></a> <br />_Figure 9 - Query of Madonna with the child, by Fra Filippo Lippi, table 46. We observe how by strengthening the pattern we can get rid of undesired results._
<p style="text-align: justify;">The pattern of the raised arms is found also in table 2 (Figure 6). When querying the <em>Andromeda</em> (7a), incredibly the <em>Farnese Atlas</em> (6a) shows up, even though it has no visual similarity. The only thing that can explain its finding is the fact that his arms are spread in a similar way as the <em>Andromeda</em>. By adding the <em>Cepheus</em> (7f), <em>Perseus</em> (7c), and <em>Farnese Atlas</em> (6a) to the query, the theme of open arms becomes evident. This means that the CNNs were able to recognize and extract the only common pattern that is visible among the four images: the path of <em>open arms</em> (Figure 10).</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/04/PP3_Fig3.png"><img class=" wp-image-5711" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/04/PP3_Fig3-204x300.png" alt="Figure 3 - Result of the query: 6a, 7a, 7c, 7d, 7f" width="677" height="996" /></a> <br />_Figure 10 - Result of the query from table 2: 6a, 7a, 7c, 7f._
<p style="text-align: justify;">It is surprising to see that the theme of <em>open arms</em> was recognised in such a variety of images: we have paintings, statues, and drawings. Here we have another example of the power of feature extraction from multiple images. The user can really guide the CNNs to the desired pattern, by querying at the same time multiple images associated to the desired pattern.</p>

<h3 style="text-align: justify;"><strong>Other visual patterns</strong></h3>
<p style="text-align: justify;">When launching <em>The Presentation of the Virgin in the Temple</em> (Figure 11), the CNNs recognize the arch and report a series of images containing arches. What is surprising is that it even recognizes arches that are not parallel to the observer, recognizing the perspective of the arch (such as those in figure 11). In addition, we see the recurrence of the architectural feature of the arch, which is a common pattern in lots of images throughout Warburg’s Bilderatlas.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Arches.png"><img class=" wp-image-6112" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Arches-300x145.png" alt="Query of &quot;Presentation of virgin at the temple, by Fra Carnevale, table 46." width="654" height="316" /></a> <br />_Figure 11 - Query of Presentation of virgin at the temple, by Fra Carnevale, table 46._
<p style="text-align: justify;">In table 46 we find the <em>Giovanna degli Albizzi Tornabuoni Medallion</em>, by Niccolò Fiorentino: in our database we have both the single medallion with Tornabuoni’s face and the photo with both the sides of the medallion. When launching the single medallion with Tornabuoni’s face, we find only medallions in the first 40 results (Figure 12). Only in the low scores with find images with double medallions, included the same medal. This indicates that the CNN pattern does not focus on the single details, so it does not see that the woman figure is the same.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Single-medallion-1.png"><img class=" wp-image-6133" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Single-medallion-1-262x300.png" alt="Figure BOH - Query of Tornabuoni medallion, by Niccolò Spinelli, table 46." width="674" height="772" /></a> <br />_Figure 12 - Query of Tornabuoni medallion, by Niccolò Spinelli, table 46._
<p style="text-align: justify;">In Figure 12 we see that the first results are all very similar to the medal because they come from authors contemporary to Niccolò Spinelli, who operated around 1450, such as Pietro Da Fano and Matteo de' Pasti, whose medallion is extremely similar, but turned the opposite way with respect to Spinelli’s. It is interesting that the algorithm reported this medallion as the most similar one, even if the represented figure is flipped. We find also medals from other epochs, which share a visible common pattern: a head enclosed in a medallion, where at the borders we find some texts.</p>
<p style="text-align: justify;">When launching the double medallion of Tornabuoni, we get only double medallions (Figure 13). Here, the found medallions with similarities with respect to Spinelli’s medallion are present in a larger number, probably because in the database most of the medallions are double. The first result is a medal from Niccolò Spinelli himself, and the next five results are medallions from Pisanello, his contemporary. The styles are extremely similar.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Double-medallion.png"><img class=" wp-image-6115" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Double-medallion-300x270.png" alt="Figure BOH - Query of Tornabuoni medallion, by Niccolò Spinelli, table 46. Both the faces of the medal were queried." width="668" height="601" /></a> <br />_Figure 13 - Query of Tornabuoni medallion, by Niccolò Spinelli, table 46. Both the faces of the medal were queried._
<h3 style="text-align: justify;"><strong>Table 45: Static vs dynamic scenes</strong></h3>
<p style="text-align: justify;">In this table we find the most interesting results. The theme of the table can be explained by simply putting together the two central paintings: <em>Appearance of the Angel to Zacharia</em> (Figure 14), and <em>Slaughter of the Innocents</em> (Figure 15), both by Ghirlandaio. They are similar, but at the same time with a basic difference: both show the same architectonic element (the arch) in the background, and a scene in front; however, while one scene is static and calm, the other is dynamic and agitated. One indeed represents purity, while the other represents a war scene.</p>
<p style="text-align: justify;">One might imagine that the architectural figure of the arch would be the predominant feature, and thus the results of the two queries would be extremely similar. Surprisingly, the CNNs are able to distinguish the difference between the two types of scenes! While for one research we find dynamic scenes, mostly violent, for the other we find very static calm scenes, mostly religious. It is remarkable to see that CNNs recognized these two differences. This is a proof that the characterization array computed from the images really describes the painting as a whole.</p>
<p style="text-align: justify;">By launching<em> Appearance of the Angel to Zacharia</em>, in the first ten results we find both <em>Herod’s Banquet</em> (also present in table 45). Therefore, we strengthen the pattern with <em>Herod's banquet</em>, and launch a new query. The pattern becomes clear: an arch in the background that overlooks at a scene with several (mostly static) figures (Figure 14<strong>)</strong>. Interestingly, there are also several paintings containing a static scene with only a few figures (mostly two figures), probably due to the architectonic element in the background.</p>
<p style="text-align: justify;">We find several paintings from Fra Filippo Lippi and Ghirlandaio. Those from Ghirlandaio are all from Santa Maria Novella in Florence and thus present some clear visual similarities: same style both for the architectonic elements and figures.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Calm_scenes.png"><img class=" wp-image-6116" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Calm_scenes-175x300.png" alt="Figure BOH - Query of static scenes, table 45." width="615" height="1054" /></a> <br />_Figure 14 - Query of static scenes, table 45._
<p style="text-align: justify;">When launching the <em>Slaughter of the Innocents</em>, the results show a great number of violent scenes in the foreground, with an arch in the background. Only a small amount of static scenes is reported, although with lower scores. We find the <em>Slaughter of the Innocents</em>, by Matteo Di Giovanni, which is also present in table 45.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Slaughter_Innocents_TOT-1.png"><img class=" wp-image-6132" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Slaughter_Innocents_TOT-1-300x172.png" alt="Figure BOH - Query of dynamic scenes, table 45." width="687" height="394" /></a> <br />_Figure 15 - Query of dynamic scenes, table 45._
<p style="text-align: justify;">In table 45 we see the feature of the arch in most of the images. We thus see the recurrence of the theme of the power across the Bilderatlas.</p>

<h3 style="text-align: justify;"><strong>Table 46: The fruit-bearing nymph</strong></h3>
<p style="text-align: justify;">In table 46, the most representative image is a detail from <em>The Birth of St John the Baptist, </em>by Ghirlandaio. We search for this theme in the database.</p>
<p style="text-align: justify;">We lunched it together with a detail from the <em>Three Temptations of Christ</em> of Botticelli, since the the two women carrying flowers resemble to each other. It is interesting to observe that a few paintings that have very similar figures come out (Figure 16). These paintings are not in the table, so they can nicely represent a continuation: <em>Moses's Journey into Egypt and the Circumcision of His Son Eliezer, </em>by Pietro Perugino, and <em>Madonna with the Child and Scenes from the Life of St Anne</em>, by Fra Filippo Lippi. The woman represented in the latter painting is extremely similar. We find that Fra Filippo operated some years before Ghirlandaio, so the latter was probably inspired by the former for the figure of the nymph, although with a different interpretation. In the row just below the reported scores, we also find Michelangelo's <em>Judith and Holofernes</em> (Figure 17).</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/nymph_group-1.png"><img class=" wp-image-6126" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/nymph_group-1-300x175.png" alt="Figure BOH - Query of the nymph, table 46. In this case the nymph from &quot;Three temptations of Christ&quot; is in the middle of a crowd." width="681" height="397" /></a> <br />_Figure 16 - Query of the nymph, table 46. In this case the nymph from "Three temptations of Christ" is in the middle of a crowd._
<br /><a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Screen-Shot-2016-05-31-at-16.23.18.png"><img class="size-medium wp-image-6120 " src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/Screen-Shot-2016-05-31-at-16.23.18-201x300.png" alt="Figure BOH - &quot;Judith and Holofernes (detail)&quot;, by Michelangelo Buonarroti." width="201" height="300" /></a> <br />_Figure 17 - "Judith and Holofernes (detail)", by Michelangelo Buonarroti._
<p style="text-align: justify;">In this query, the nymph-like woman in <em>Three temptations of Christ</em> was in the middle of a crowd. We thus get many paintings with agglomerates of figures in movement where the dark-light of the clothes is present on many characters (for example, S<em>t John the Evangelist Resuscitating Drusiana</em>, by Filippo Lippi, in Figure 17). However, if we launch only the details with the single women (Figure 18), we find paintings like<strong> </strong><em>The Beguiling of Merlin, </em>by Edward Burne-Jones. It is interesting to notice that this painting was reported despite the totally different style. Indeed, the figure is clearly nymph-like. Also Michelangelo's <em>Judith and Holofernes</em> is present in the results of this query. In the lower scores, together with Michelangelo's <em>Judith and Holofernes, </em>we found Botticelli's <em>The trial and calling of Moses</em> (Figure 19). We noticed that the <em>Allegory of August</em>, by Cosmé Tura (Figure 19) was reported. This fresco belonged to the pattern of <em>open arms</em>, seen in table 2, and it can thus represent a link between table 2 and 46.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/nymph_single.png"><img class=" wp-image-6122" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/nymph_single-300x181.png" alt="Figure BOH - Query of the nymph, table 46. In this case the nymph from &quot;Three temptations of Christ&quot; occupies the whole queried detail." width="690" height="416" /></a> <br />_Figure 18 - Query of the nymph, table 46. In this case the nymph from "Three temptations of Christ" occupies the whole queried detail._
<p style="text-align: justify;">Also in this query we can see that the light-dark contrast of the clothes has a major importance when launching the single nymph. Several statues are reported due to this, and they are not necessarily in movement.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/nymph_single2.png"><img class=" wp-image-6130" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/nymph_single2-300x214.png" alt="Figure BOH - Additional results from the query of the nymph." width="458" height="327" /></a> <br />_Figure 19 - Additional results from the query of the nymph._
<p style="text-align: justify;">Overall, we can say that the CNNs is probably not the best solution to find single details like this in a large image, since the computed feature array describes the painting as a whole. We cannot launch the whole painting because the pattern will not describe the single woman. CNNs can however be useful to find a figure in the cases where it covers most of the painting, because the computed feature would describe the woman. Therefore, to find the single nymph, one has to extract the detail from the painting and launch it.</p>
<p style="text-align: justify;">In table 46 we find two other nymph-like figures (Figure 20). They are two drawings, with women carrying vases. Despite the strong similarities with the nymph in <em>The Birth of St John the Baptist,</em> no other nymph-like figures were reported querying the two drawings (both together and separately). This is probably because paintings and drawings are too different from the CNN standpoint. The background has indeed a strong influence when querying an image, and we have a proof when we query one drawing at a time. We mainly find other drawings whose background is similar. The other <em>Woman carrying vase</em> is reported, but with a considerable lower score.</p>
<p style="text-align: justify;">We saw such a strong influence of the background also when querying the miniatures from table 2.</p>
<a href="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/women-carrying-vases.png"><img class=" wp-image-6127" src="http://veniceatlas.epfl.ch/wp-content/uploads/2016/05/women-carrying-vases-300x212.png" alt="Figure BOH - Women carrying vases, table 46." width="490" height="346" /></a> <br />_Figure 20 - Women carrying vases, table 46._
<h2 style="text-align: justify;"><strong>Conclusion</strong></h2>
<p style="text-align: justify;">To conclude, the strengths of this algorithm originate from the extraction of a low-level characterization of the images. The possibility of constructing a common feature by launching more images at the same time allows the user to guide the algorithm towards the desired pattern.</p>
<p style="text-align: justify;">The algorithm proved to be extremely successful as far as strong visual patterns are concerned. In some cases, images with extremely similar styles were reported, and the artists were found indeed to have operated in the same epoch.</p>
<p style="text-align: justify;">Some surprising results were achieved with the pattern of the open arms in table 2, and the two contrasting paintings in table 45. Several different patterns were explored, and the CNN found a high number of other images that could fit well in Warburg's tables. The algorithm was also able to find connections between different tables, such as in the case of Tura's <em>Allegory of August.</em></p>
<p style="text-align: justify;">With the help of “negative” images, this algorithm can become even more powerful.</p>


<hr />
<h2 style="text-align: justify;"><strong>References</strong></h2>
<p style="text-align: justify;">[1]         <a href="http://en.wikipedia.org/wiki/Aby_Warburg"> http://en.wikipedia.org/wiki/Aby_Warburg</a></p>
<p style="text-align: justify;">[2]         Isabella di Lenardo, Benoit Seguin, Frédéric Kaplan. Visual Patterns Discovery in Large Databases of Paintings<strong>.</strong></p>
<p style="text-align: justify;">[3]         <a href="http://www.engramma.it/eOS2/atlante/">http://www.engramma.it/eOS2/atlante/</a></p>
<p style="text-align: justify;">[4]         L’Atlas Mnémosyne, Aby Warburg, <strong>2012</strong>, <em>L’écarquillé.</em></p>
<p style="text-align: justify;">[5]         <a href="http://warburg.library.cornell.edu">http://warburg.library.cornell.edu</a></p>
