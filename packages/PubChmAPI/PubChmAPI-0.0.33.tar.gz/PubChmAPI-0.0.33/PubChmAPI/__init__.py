print("This Python package, PubChemAPI, simplifies the interaction with the PubChem database, allowing users to seamlessly retrieve information related to compounds, substances, assays, proteins, genes, and more.\nWhether you're a researcher, scientist, or developer, this package provides an easy-to-use interface to access a wealth of information stored in PubChem.\n\nCreated by Ahmed Alhilal.\nContact: aalhilal@kfu.edu.sa\n\nSource:\n1. https://chem.libretexts.org/Courses/Intercollegiate_Courses/Cheminformatics/01%3A_Introduction (Free ebook)\n2. https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest#section=Dates\n\nExplore the functions inside this package:\nhttps://docs.google.com/spreadsheets/d/1Lc6dTcneR2KLtnT3zkLMn7jPOlFOznIy/edit?usp=sharing&ouid=112811379287189098377&rtpof=true&sd=true\n\nGitHub Repository:\nhttps://github.com/ahmed1212212/PubChemAPI.git")

"""# compound"""

def generate_pubchem_url(input_type, input_identifier, output_type, output_format, *input_data):
    """
    Generate a PubChem URL based on input specifications.

    Args:
    - input_type (str): Type of input identifier (e.g., 'cid', 'aid', 'sid').
    - input_identifier (str): Input identifier to convert to other formulas.
    - output_type (str): Type of output specification (e.g., 'record', 'description', 'assaysummary').
    - output_format (str): Output format option (e.g., 'xml', 'csv', 'png').
    - *input_data: Variable-length input data (e.g., list of identifiers, names, SMILES).

    Returns:
    - str: PubChem URL for the specified conversion.

    Example:
    generate_pubchem_url("compound", "cid", "sids", "xml", 180)
    """
    input_type_str = str(input_type)
    input_identifier_str = str(input_identifier)
    output_type_str = str(output_type)
    output_format_str = str(output_format)
    # Convert input data to a flat list of strings
    input_data_strings = [str(item) for sublist in input_data for item in (sublist if isinstance(sublist, list) else [sublist])]

    # Join the input data into a comma-separated string
    input_data_str = ",".join(input_data_strings)

    # Construct the URL
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/{input_type_str}/{input_identifier_str}/{input_data_str}/{output_type_str}/{output_format_str}"

    return url
