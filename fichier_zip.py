import zipfile
import shutil

"""fichier_zip = zipfile.ZipFile("fichiers_excel.zip", "w")
fichier_zip.write("octobre.xlsx")
fichier_zip.write("novembre.xlsx")
fichier_zip.write("decembre.xlsx")
fichier_zip.write("fichier_json.txt")
fichier_zip.write("fichier_sortie.pdf")
fichier_zip.write("presentation.pdf")
fichier_zip.write("recap.pdf")
fichier_zip.write("text_ficher.txt")
fichier_zip.write("Total_ventes_trimestre.xlsx")
fichier_zip.close()"""

shutil.make_archive("fichiers_excel2", "zip", "fichiers_excel")