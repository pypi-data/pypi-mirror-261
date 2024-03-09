import haitch as H

from poaster.bulletin import schemas, services
from poaster.core import components, config


def post_form_new() -> H.Element:
    """Form for adding a new post."""
    return H.form(id_="newPost", action="/posts/new", method="post")(
        H.h1("Add new post"),
        H.label(for_="title")("Title:"),
        H.input(id_="title", type_="text", name="title"),
        H.label(for_="text")("Text:"),
        H.textarea(id_="text", name="text", rows=8),
        H.br(),
        H.a(href="/posts", style="padding-right: 1.5rem;")("Back"),
        H.button(type_="submit")("Save"),
    )


def post_form_edit(post: schemas.PostSchema) -> H.Element:
    """Form for editing a post."""
    return H.form(id_="editPost", action=f"/posts/{post.id}/edit", method="post")(
        H.h1("Edit post"),
        H.label(for_="title")("Title:"),
        H.input(id_="title", type_="text", name="title", value=post.title),
        H.label(for_="text")("Text:"),
        H.textarea(id_="text", name="text", rows=8)(post.text),
        H.br(),
        components.links([{"name": "Back", "href": f"/posts/{post.id}", "show": True}]),
        H.button(type_="submit")("Save"),
    )


def post_form_delete(post: schemas.PostSchema) -> H.Element:
    """Form for editing a post."""
    return H.form(id_="deletePost", action=f"/posts/{post.id}/delete", method="post")(
        H.h1("Delete post"),
        components.message(
            "Are you sure you want to permanently delete this post?", variant="danger"
        ),
        H.br(),
        components.links([{"name": "Back", "href": f"/posts/{post.id}", "show": True}]),
        H.button(type_="submit")("Confirm"),
    )


async def post_list(bulletin_service: services.BulletinService) -> H.Child:
    """List of stored posts."""
    if not (posts := await bulletin_service.get_posts()):
        return components.message("No posts were found.", variant="warning")

    return [
        H.section(
            H.h2(post.title),
            await post_meta_info(bulletin_service, post),
            post_text_snippet(
                post.text,
                max_word_count=config.settings.post_snippet_max_word_count,
            ),
            H.a(href=f"/posts/{post.id}")("View"),
        )
        for post in posts
    ]


async def post_detail(
    bulletin_service: services.BulletinService, post: schemas.PostSchema, username: str
) -> H.Element:
    """Detail regarding a post."""
    return H.fragment(
        H.h1(post.title),
        await post_meta_info(bulletin_service, post),
        H.p(post.text),
        H.br(),
        components.links(
            [
                {
                    "name": "Back",
                    "href": "/posts",
                    "show": True,
                },
                {
                    "name": "Edit",
                    "href": f"/posts/{post.id}/edit",
                    "show": username != "",
                },
                {
                    "name": "Delete",
                    "href": f"/posts/{post.id}/delete",
                    "show": username != "",
                },
            ]
        ),
    )


def post_text_snippet(text: str, *, max_word_count: int) -> H.Element:
    """Text snippet of a post's text."""
    subset = " ".join(text.split()[: max(max_word_count, 0)])
    return H.p(text if subset == text else subset + "…")


async def post_meta_info(
    bulletin_service: services.BulletinService, post: schemas.PostSchema
) -> H.Element:
    """Meta information regarding a post."""
    latest_post = await bulletin_service.get_latest_version_of_post(id=post.id)
    updated_at_str = latest_post.updated_at.strftime("%b %d, %Y at %H:%M")
    return H.small(f"Last updated on {updated_at_str} UTC")
