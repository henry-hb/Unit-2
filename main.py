from PIL import Image, ImageFilter, ImageEnhance

orange_cat = Image.open(r"orange_tabby.jpg")
blurry_cat = orange_cat.filter(ImageFilter.GaussianBlur(20))
blurry_cat.save(r"blurry_cat.jpg")
bw_cat = ImageEnhance.Color(orange_cat).enhance(0).save(r"bw_cat.jpg")
bright_cat = ImageEnhance.Color(orange_cat).enhance(10).save(r"bright_cat.jpg")

#hw portion

spinny_cat = orange_cat.rotate(58, expand = True)
spinny_cat.save(r"spinny_cat.jpg")

gray_cat = orange_cat.convert("L")
edges = gray_cat.filter(ImageFilter.FIND_EDGES)
less_detailed_cat = gray_cat.filter(ImageFilter.SMOOTH)
smooth_edges_cat = less_detailed_cat.filter(ImageFilter.FIND_EDGES)
enhanced_edges_cat = smooth_edges_cat.filter(ImageFilter.EDGE_ENHANCE)
enhanced_edges_cat.save(r"enhanced_edges_cat.jpg")

embossed_cat = gray_cat.filter(ImageFilter.EMBOSS)
embossed_cat.save(r"embossed_cat.jpg")