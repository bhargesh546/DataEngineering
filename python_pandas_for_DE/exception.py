import pandas as pd

def analyze_series(s):
    """Analyze pandas Series.
    
    Demonstrates assertions and exception handling.
    """
    
    # Validate inputs
    assert isinstance(s, pd.Series), "Input must be a pandas Series"  

    try:
        # Attempt processing 
        mean = s.mean()  
        median = s.median()

    # Catch errors    
    except Exception as e:   
        # Manually raise exception
        raise ValueError("Error analyzing series") from e  

    # Assert reasonable results       
    assert (mean > 0) & (median > 0), "Mean and median are invalid!"
    
    return mean, median
    
s = pd.Series([1, 2, 3])
print(analyze_series(s))