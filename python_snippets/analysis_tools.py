def print_all_columns(df):
  return HTML('<br />'.join(str(y) for y in df.columns))