from __future__ import annotations
import nuri.core._core
import os
__all__ = ['MoleculeReader', 'readfile', 'readstring']
class MoleculeReader:
    def __iter__(self) -> MoleculeReader:
        ...
    def __next__(self) -> nuri.core._core.Molecule:
        ...
def readfile(fmt: str, path: os.PathLike, sanitize: bool = True, skip_on_error: bool = False) -> MoleculeReader:
    """
    Read a molecule from a file.
    
    :param fmt: The format of the file.
    :param path: The path to the file.
    :param sanitize: Whether to sanitize the produced molecule. Note that if the
      underlying reader produces a sanitized molecule, this option is ignored and
      the molecule is always sanitized.
    :param skip_on_error: Whether to skip a molecule if an error occurs, instead of
      raising an exception.
    :raises OSError: If any file-related error occurs.
    :raises ValueError: If the format is unknown or sanitization fails, unless
      `skip_on_error` is set.
    :rtype: collections.abc.Iterable[Molecule]
    """
def readstring(fmt: str, data: str, sanitize: bool = True, skip_on_error: bool = False) -> MoleculeReader:
    """
    Read a molecule from string.
    
    :param fmt: The format of the file.
    :param data: The string to read.
    :param sanitize: Whether to sanitize the produced molecule. Note that if the
      underlying reader produces a sanitized molecule, this option is ignored and
      the molecule is always sanitized.
    :param skip_on_error: Whether to skip a molecule if an error occurs, instead of
      raising an exception.
    :raises ValueError: If the format is unknown or sanitization fails, unless
      `skip_on_error` is set.
    :rtype: collections.abc.Iterable[Molecule]
    
    The returned object is an iterable of molecules.
    
    >>> for mol in nuri.readstring("smi", "C"):
    ...     print(mol[0].atomic_number)
    6
    """
