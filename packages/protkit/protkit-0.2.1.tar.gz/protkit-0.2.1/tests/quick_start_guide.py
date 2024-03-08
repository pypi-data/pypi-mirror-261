def quick_start_example():
    from protkit.download import Download
    from protkit.file_io import PDBIO, ProtIO
    from protkit.properties import DihedralAngles, SurfaceArea

    # Download a PDB file from the RCSB PDB database and save it to a file.
    Download.download_pdb_file_from_rcsb("1ahw", "1ahw.pdb")

    # Load a PDB file into a Protein object.
    protein = PDBIO.load("1ahw.pdb")[0]

    # Print the number of chains in the protein.
    print(protein.num_chains)

    # Keep only the A and B chains
    protein.keep_chains(["A", "B"])
    print(protein.get_chain('A').sequence)

    # Do a bit of cleanup, by removing any hetero atoms and fixing disordered atoms.
    protein.remove_hetero_residues()
    protein.fix_disordered_atoms()

    # Compute dihedral angles for the protein, and assign them as extended attributes to residues.
    DihedralAngles.dihedral_angles_of_protein(protein, assign_attribute=True)
    print(protein.get_chain('A').get_residue(1).get_attribute('dihedral_angles')['PHI'])

    # Compute surface areas for the protein. Surface areas are automatically computed and assigned
    # at the residue, chain and protein level.
    SurfaceArea.surface_area_of_protein(protein, assign_attribute=True)
    print(protein.get_attribute('surface_area'))

    # Save the protein to a protkit (.prot) file.  All attributes, such as the
    # computed dihedral angles and surface areas, will be saved as well and
    # is available for later retrieval!
    protein.set_attribute("note", "Experimenting with Protkit")
    ProtIO.save(protein, "1ahw.prot")
    protein2 = ProtIO.load("1ahw.prot")[0]
    print(protein2.get_attribute('surface_area'))
    print(protein2.get_attribute('note'))

def download_pdb_example():
    from protkit.download import Download

    # Download a PDB file from the RCSB PDB database and save it to a file.
    Download.download_pdb_file_from_rcsb("1ahw", "data/pdb_files/rcsb/1ahw.pdb")

    # Download a PDB file from the SAbDab database and save it to a file.
    Download.download_pdb_file_from_sabdab("1ahw", "data/pdb_files/sabdab/1ahw.pdb")

    # Download multiple PDB files from the RCSB PDB in parallel and save them to a directory.
    Download.download_pdb_files_from_rcsb(["1ahw", "1a4y", "1a6m"], "data/pdb_files/rcsb/", n_jobs=3)

def download_fasta_example():
    from protkit.download import Download

    # Download a Fasta file from the Uniprot database and save it to a file.
    Download.download_fasta_file_from_uniprot("P12345", "data/fasta_files/uniprot/P12345.xml")

    # Download multiple Fasta files from the RCSB database in parallel and save them to a directory.
    Download.download_fasta_files_from_rcsb(["P12345", "P12346", "P12347"], "data/fasta_files/rcsb/")

    # Download multiple Fasta files from the Uniprot database in parallel and save them to a directory.
    Download.download_fasta_files_from_uniprot(["P12345", "P12346", "P12347"], "data/fasta_files/rcsb/")


def download_cif_example():
    from protkit.download import Download

    # Download a CIF file from the RCSB PDB database and save it to a file.
    Download.download_cif_file_from_rcsb("1ahw", "data/cif_files/rcsb/1ahw.cif")

    # Download multiple CIF files from the RCSB PDB database in parallel and save them to a directory.
    Download.download_cif_files_from_rcsb(["1ahw", "1a4y", "1a6m"], "data/cif_files/rcsb/")

    # Download a binary CIF file from the RCSB PDB database and save it to a file.
    Download.download_binary_cif_file_from_rcsb("1ahw", "data/cif_files/rcsb/1ahw.bcif")

    # Download multiple binary CIF files from the RCSB PDB database in parallel and save them to a directory.
    Download.download_binary_cif_files_from_rcsb(["1ahw", "1a4y", "1a6m"], "data/cif_files/rcsb/")

def prep_data():
    from protkit.download import Download
    from protkit.file_io import ProtIO

    # Download a PDB file from the RCSB PDB database and save it to a file.
    Download.download_pdb_file_from_rcsb("1ahw", "1ahw.pdb")

    # Load a PDB file into a Protein object.
    ProtIO.convert("1ahw.pdb", "1ahw.prot")

    # Download a FASTA file from RCSB PDB and save it to file.
    Download.download_fasta_file_from_rcsb("1ahw", "1ahw.fasta")

def properties_hydrophobicity():
    from protkit.file_io import ProtIO
    from protkit.properties import Hydrophobicity

    protein = ProtIO.load("1ahw.prot")[0]
    Hydrophobicity.hydrophobicity_of_protein(protein, assign_attribute=True)

    print(protein.get_attribute("hydrophobicity"))
    print(protein.get_chain("A").get_attribute("hydrophobicity"))
    print(protein.get_chain("B").get_attribute("hydrophobicity"))
    print(protein.get_chain("A").get_residue(0).get_attribute("hydrophobicity"))


def properties_hydrophobicity_class():
    from protkit.file_io import ProtIO
    from protkit.properties import Hydrophobicity

    protein = ProtIO.load("1ahw.prot")[0]
    Hydrophobicity.hydrophobicity_classes_of_protein(protein, assign_attribute=True)
    print(Hydrophobicity.HYDROPHOBICITY_CLASS_STRING[protein.get_chain("A").get_residue(0).get_attribute("hydrophobicity_class")])


def properties_mass():
    from protkit.file_io import ProtIO
    from protkit.properties import Mass

    protein = ProtIO.load("1ahw.prot")[0]
    Mass.residue_mass_of_protein(protein, assign_attribute=True)
    Mass.atomic_mass_of_protein(protein, assign_attribute=True)
    Mass.molecular_mass_of_protein(protein, assign_attribute=True)

    residue = protein.get_chain("A").get_residue(0)
    print(residue.get_attribute("residue_mass"))
    print(residue.get_attribute("atomic_mass"))
    print(residue.get_attribute("molecular_mass"))


def properties_chemical_class():
    from protkit.file_io import ProtIO
    from protkit.properties import ChemicalClass

    protein = ProtIO.load("1ahw.prot")[0]
    ChemicalClass.chemical_classes_of_protein(protein, assign_attribute=True)
    print(ChemicalClass.CHEMICAL_CLASS_STRING[protein.get_chain("A").get_residue(0).get_attribute("chemical_class")])


def properties_charge():
    from protkit.file_io import ProtIO
    from protkit.properties import Charge

    protein = ProtIO.load("1ahw.prot")[0]
    Charge.charge_of_protein(protein, assign_attribute=True)
    chain = protein.get_chain("A")
    residue = chain.get_residue(0)
    print(protein.get_attribute("charge"))
    print(chain.get_attribute("charge"))
    print(residue.get_attribute("charge"))


def properties_polarity():
    from protkit.file_io import ProtIO
    from protkit.properties import Polarity

    protein = ProtIO.load("1ahw.prot")[0]
    Polarity.polarities_of_protein(protein, assign_attribute=True)
    residue = protein.get_chain("A").get_residue(0)
    print(Polarity.POLARITY_STRING[residue.get_attribute("polarity")])


def properties_donors_acceptors():
    from protkit.file_io import ProtIO
    from protkit.properties import DonorsAcceptors

    protein = ProtIO.load("1ahw.prot")[0]

    DonorsAcceptors.donor_residues_of_protein(protein, assign_attribute=True)
    DonorsAcceptors.acceptor_residues_of_protein(protein, assign_attribute=True)
    residue = protein.get_chain("A").get_residue(0)
    print(residue.get_attribute("is_donor_residue"))
    print(residue.get_attribute("is_acceptor_residue"))

    DonorsAcceptors.donor_atoms_of_protein(protein, assign_attribute=True)
    DonorsAcceptors.acceptor_atoms_of_protein(protein, assign_attribute=True)
    atom = protein.get_chain("A").get_residue(0).get_atom("N")
    print(atom.get_attribute("is_donor_atom"))
    print(atom.get_attribute("is_acceptor_atom"))


def properties_surface_area():
    from protkit.file_io import ProtIO
    from protkit.properties import SurfaceArea

    protein = ProtIO.load("1ahw.prot")[0]
    chain = protein.get_chain("A")
    residue = chain.get_residue(0)

    SurfaceArea.surface_area_of_protein(protein, assign_attribute=True)
    print(protein.get_attribute("surface_area"))
    print(chain.get_attribute("surface_area"))
    print(residue.get_attribute("surface_area"))


def properties_volume():
    from protkit.file_io import ProtIO, FastaIO
    from protkit.properties import Volume

    protein = ProtIO.load("1ahw.prot")[0]
    chain = protein.get_chain("A")
    residue = chain.get_residue(0)

    Volume.volume_of_protein(protein, assign_attribute=True)
    print(protein.get_attribute("volume"))
    print(chain.get_attribute("volume"))
    print(residue.get_attribute("volume"))

    sequence = FastaIO.load("1ahw.fasta")[0]
    Volume.volume_of_sequence(sequence, assign_attribute=True)
    print(sequence.get_attribute("volume"))


def properties_volume_class():
    from protkit.file_io import ProtIO, FastaIO
    from protkit.properties import Volume

    protein = ProtIO.load("1ahw.prot")[0]
    residue = protein.get_chain("A").get_residue(0)

    Volume.volume_classes_of_protein(protein, assign_attribute=True)
    print(Volume.VOLUME_CLASS_STRING[residue.get_attribute("volume_class")])

    sequence = FastaIO.load("1ahw.fasta")[0]
    Volume.volume_classes_of_sequence(sequence, assign_attribute=True)
    for volume_class in sequence.get_attribute("volume_class"):
        print(Volume.VOLUME_CLASS_STRING[volume_class])


def properties_bounds_and_center():
    from protkit.file_io import ProtIO
    from protkit.properties import Bounds

    protein = ProtIO.load("1ahw.prot")[0]
    chain = protein.get_chain("A")
    residue = chain.get_residue(0)

    Bounds.bounds_of_protein(protein, assign_attribute=True)
    Bounds.center_of_protein(protein, assign_attribute=True)

    print(protein.get_attribute("bounds"))
    print(chain.get_attribute("bounds"))
    print(residue.get_attribute("bounds"))

    print(protein.get_attribute("center"))
    print(chain.get_attribute("center"))
    print(residue.get_attribute("center"))


def properties_bond_lengths():
    from protkit.file_io import ProtIO
    from protkit.properties import BondLengths

    protein = ProtIO.load("1ahw.prot")[0]
    residue = protein.get_chain("A").get_residue(0)

    BondLengths.bond_lengths_of_protein(protein, assign_attribute=True)
    for (atom1, atom2), length in residue.get_attribute("bond_lengths").items():
        print(f"{atom1}-{atom2}: {length}")


def properties_peptide_lengths():
    from protkit.file_io import ProtIO
    from protkit.properties import BondLengths

    protein = ProtIO.load("1ahw.prot")[0]
    chain = protein.get_chain("A")

    BondLengths.peptide_bond_lengths_of_protein(protein, assign_attribute=True)
    print(chain.get_attribute("peptide_bond_lengths"))


def properties_bond_angles():
    from protkit.file_io import ProtIO
    from protkit.properties import BondAngles

    protein = ProtIO.load("1ahw.prot")[0]
    residue = protein.get_chain("A").get_residue(0)

    BondAngles.bond_angles_of_protein(protein, assign_attribute=True)
    for (atom1, atom2, atom3), angle in residue.get_attribute("bond_angles").items():
        print(f"{atom1}-{atom2}-{atom3}: {angle}")


def properties_dihedral_angles():
    from protkit.file_io import ProtIO
    from protkit.properties import DihedralAngles

    protein = ProtIO.load("1ahw.prot")[0]
    residue = protein.get_chain("A").get_residue(1)

    DihedralAngles.dihedral_angles_of_protein(protein, assign_attribute=True)
    for angle_name, angle in residue.get_attribute("dihedral_angles").items():
        print(f"{angle_name}: {angle}")


def properties_circular_variance():
    from protkit.file_io import ProtIO
    from protkit.properties import CircularVariance

    protein = ProtIO.load("1ahw.prot")[0]
    residue = protein.get_chain("A").get_residue(1)
    atom = residue.get_atom("CA")

    CircularVariance.circular_variance_by_residue(protein, assign_attribute=True)
    print(residue.get_attribute("cv_residue"))

    CircularVariance.circular_variance_by_atom(protein, assign_attribute=True)
    print(atom.get_attribute("cv_atom"))


def properties_interface_atoms():
    from protkit.file_io import ProtIO
    from protkit.properties import Interface

    protein = ProtIO.load("1ahw.prot")[0]
    atoms1 = list(protein.filter_atoms(chain_criteria=[("chain_id", ["A", "B"])]))
    atoms2 = list(protein.filter_atoms(chain_criteria=[("chain_id", ["C"])]))

    Interface.interface_atoms(atoms1, atoms2, cutoff=5.0, assign_attribute=True)
    for atom in atoms1:
        if atom.get_attribute("in_interface"):
            print(atom.id)


def properties_interface_residues():
    from protkit.file_io import ProtIO
    from protkit.properties import Interface

    protein = ProtIO.load("1ahw.prot")[0]
    residues1 = list(protein.filter_residues(chain_criteria=[("chain_id", ["A", "B"])]))
    residues2 = list(protein.filter_residues(chain_criteria=[("chain_id", ["C"])]))

    Interface.interface_residues(residues1, residues2, cutoff=5.0, assign_attribute=True)
    Interface.interface_residues_from_alpha_carbon(residues1, residues2, cutoff=6.0, assign_attribute=True, key="ca_in_interface")

    for residue in residues1:
        if residue.get_attribute("in_interface"):
            print(residue.id)

    for residue in residues1:
        if residue.get_attribute("ca_in_interface"):
            print(residue.id)

# prep_data()

# quick_start_example()
# download_pdb_example()
# download_fasta_example()
# download_cif_example()

# properties_hydrophobicity()
# properties_hydrophobicity_class()
# properties_mass()
# properties_chemical_class()
# properties_charge()
# properties_polarity()
# properties_donors_acceptors()
# properties_surface_area()
# properties_volume()
# properties_volume_class()
# properties_bounds_and_center()
# properties_bond_lengths()
# properties_peptide_lengths()
# properties_bond_angles()
# properties_dihedral_angles()
# properties_circular_variance() -> double check first residue
# properties_interface_atoms()
# properties_interface_residues()