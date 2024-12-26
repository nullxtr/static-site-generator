import os
from inline_markdown import extract_title
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        content = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    html_string = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    with open(dest_path, "w") as file:
        file.write(final_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_content = os.listdir(dir_path_content)
    for el in dir_content:
        source_path = os.path.join(dir_path_content, el)
        if os.path.isdir(source_path):
            dest_path = os.path.join(dest_dir_path, el)
            os.mkdir(dest_path)
            generate_pages_recursive(source_path, template_path, dest_path)
        else:
            if el.endswith(".md"):
                dest_path = os.path.join(dest_dir_path, el.replace(".md", ".html"))
                generate_page(source_path, template_path, dest_path)