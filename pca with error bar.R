## script for generating PCA plot with error bars for data with biological or technical replicates
## rely on R package vegan
## Sizhong Yang (https://github.com/camel315/), 2014-10-20, Potsdam

pca_error_bar <- function(data, group, colors, siteInRow = TRUE, scale=TRUE, scl=1,...){
  message('Make sure that your data have biological or techinical replicates (>=3)')
  message('This function relies on vegan package')
  if(!require(vegan)){
    install.packages("vegan")
    library(vegan)
  }  
  message('Please specify if site names in rows and species in column')
  if(!siteInRow) {data = as.data.frame(t(data))} #transpose data if sites are not in rows
  pca <- vegan::rda(data, scale = scale)
  # get the scores value for plotting
  scrs <- as.data.frame(vegan::scores(pca, display = "sites", scaling = scl,choices = 1:2))
  # get the centeroid for each group
  cent <- do.call(rbind, lapply(split(scrs, group), colMeans))
  #or:cent <- as.data.frame(t(sapply(split(scrs, group), colMeans)))
  # get the se for each group
  serrFun <- function(df) {
    apply(df, 2, function(x) sd(x) / sqrt(length(x)))
  }
  serr <- do.call(rbind, lapply(split(scrs, group), serrFun))
  # Final step, plot centroid and se into PCA plot
  plot(pca, display = "sites", scaling = scl, type = "n",...)
  points(cent, col = colors, cex = 1.1, ...) # add centroid points
  # add error bars
  lev <- levels(group)
  for (i in seq_along(lev)) {
    arrows(cent[i, 1] - serr[i, 1], cent[i, 2], # add horizontal error bar
           cent[i, 1] + serr[i, 1], cent[i, 2], # add horizontal error bar
           col = colors[i], code = 3, angle = 90, length = 0.05)
    arrows(cent[i, 1], cent[i, 2] - serr[i, 2], # add vertical error bar
           cent[i, 1], cent[i, 2] + serr[i, 2], # add vertical error bar
           col = colors[i], code = 3, angle = 90, length = 0.05)
  }
  message("Done! Enjoy the function")
}

## ----------------------------
## example to use the function
## ----------------------------

data(varespec)
data(varechem)
grp <- with(varechem, cut(Baresoil, 4, labels = 1:4))
cols = c("red","orange","blue","forestgreen")

pca_error_bar(data = varespec,group = grp,colors=cols,main="test pca",pch=15)
