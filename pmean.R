# Normalize filename
NORMALIZE_FILENAME <- function(name) {
  l_norm <- 3L
  
  if (nchar(name) >= l_norm) {
    return(name)
    
  }
  
  name <- paste('000', name, sep = '')
  
  return(paste(substr(
    name,
    nchar(name) - l_norm + 1,
    nchar(name)
  ), '.csv', sep = ''))
}

# pmean function
pmean <- function(directory, pollutant, id = c(1:332)) {
  dir_path <-
    paste('C:/Users/Daria/Desktop/Master/R&Python/labs/5/', directory, '/', sep = "")
  values <- c()
  
  for (i in id) {
    f_buff <-
      read.csv(file = paste(dir_path, NORMALIZE_FILENAME(i), sep = ""))
    col_names <- colnames(f_buff)
    
    if (pollutant %in% col_names) {
      values <- c(values, f_buff[, pollutant, drop = TRUE])
    }
  }
  return(mean(values, na.rm = TRUE))
}

# complete function
complete <- function(directory, id) {
  dir_path <-
    paste('C:/Users/Daria/Desktop/Master/R&Python/labs/5/', directory, '/', sep = "")
  df <- data.frame(filename = character(), count = integer())
  
  for (i in id) {
    f_name <- NORMALIZE_FILENAME(i)
    
    f_buff <-
      read.csv(file = paste(dir_path, f_name, sep = ""))
    
    n <- sum(!is.na(f_buff['nitrate'] & f_buff['sulfate']))
    
    row <- list(id = f_name, nobs = n)
    df = rbind(df, row, stringsAsFactors = FALSE)
  }
  
  return(df)
}

# corr function
corr <- function(directory, threshold = 0) {
  dir_path <-
    paste('C:/Users/Daria/Desktop/Master/R&Python/labs/5/', directory, '/', sep = "")
  f_list <- list.files(dir_path)
  values <- c()
  
  for (i in f_list) {
    f_buff <-
      read.csv(file = paste(dir_path, i, sep = ""))
    n <- sum(!is.na(f_buff['nitrate'] & f_buff['sulfate']))
    
    if (n >= threshold) {
      f_subset <-
        f_buff[!is.na(f_buff$sulfate) & !is.na(f_buff$nitrate),]
      cor_value <- cor(f_subset$sulfate, f_subset$nitrate)
      values <- c(values, cor_value)
    }
  }
  return (values)
}