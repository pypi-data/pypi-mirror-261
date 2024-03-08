import collections

from strictdoc.backend.sdoc.models.document import SDocDocument
from strictdoc.backend.sdoc.models.node import (
    CompositeRequirement,
    SDocNode,
)
from strictdoc.backend.sdoc.models.section import FreeText, SDocSection
from strictdoc.core.level_counter import LevelCounter


class DocumentCachingIterator:
    def __init__(self, document):
        assert isinstance(document, SDocDocument)

        self.document = document
        self.nodes_cache = []
        self.toc_nodes_cache = []

    def invalidate_cache(self):
        self.nodes_cache.clear()
        self.toc_nodes_cache.clear()

    def table_of_contents(self):
        # TODO: Should bring the cache back or remove?
        # if len(self.toc_nodes_cache) > 0:  # noqa: ERA001
        #     yield from self.toc_nodes_cache  # noqa: ERA001
        #     return  # noqa: ERA001

        nodes_to_skip = (
            (FreeText, SDocNode)
            if not self.document.config.is_requirement_in_toc()
            else FreeText
        )

        for node in self.all_content():
            if isinstance(node, nodes_to_skip):
                continue
            if isinstance(node, SDocNode) and node.reserved_title is None:
                continue
            self.toc_nodes_cache.append(node)
            yield node

    def all_content(self):
        # TODO: Should bring the cache back or remove?
        # if len(self.nodes_cache) > 0:  # noqa: ERA001
        #     yield from self.nodes_cache  # noqa: ERA001
        #     return  # noqa: ERA001

        document = self.document
        level_counter = LevelCounter()

        task_list = collections.deque(document.section_contents)

        while True:
            if not task_list:
                break

            current = task_list.popleft()

            # If node is not whitelisted, we ignore it. Also, note that due to
            # this early return, all child nodes of this node are ignored
            # as well because they are not added to the iteration queue.
            if not current.ng_whitelisted:
                continue

            if isinstance(
                current, (SDocSection, SDocNode, CompositeRequirement)
            ):
                assert current.ng_level, f"Node has no ng_level: {current}"

                if current.ng_resolved_custom_level != "None":
                    level_counter.adjust(current.ng_level)
                    # TODO: Remove the need to do branching here.
                    current.context.title_number_string = (
                        current.ng_resolved_custom_level
                        if current.ng_resolved_custom_level
                        else level_counter.get_string()
                    )
                else:
                    # The idea is to include a section header without affecting
                    # the level of the nested elements (i.e. requirements), but
                    # keeping the section title in a dedicated row in DOC, TBL
                    # and TR/DTR views.
                    # Such an option can be very useful when dealing with source
                    # requirements documents with inconsistent sectioning (such
                    # as some technical standards/normative), that need to be
                    # included in a custom project.
                    # https://github.com/strictdoc-project/strictdoc/issues/639
                    current.context.title_number_string = ""

            self.nodes_cache.append(current)
            yield current

            if isinstance(current, SDocSection):
                task_list.extendleft(reversed(current.section_contents))

            elif isinstance(current, CompositeRequirement):
                task_list.extendleft(reversed(current.requirements))

    @staticmethod
    def specific_node_with_normal_levels(node):
        if isinstance(node, SDocSection):
            initial_content = node.section_contents
        elif isinstance(node, CompositeRequirement):
            initial_content = node.requirements
        else:
            return

        task_list = collections.deque(initial_content)

        while True:
            if not task_list:
                break

            current = task_list.popleft()

            if isinstance(
                current, (SDocSection, SDocNode, CompositeRequirement)
            ):
                # We are not interested in the nodes without level in this
                # iterator.
                if current.ng_resolved_custom_level == "None":
                    continue

            yield current

            if isinstance(current, SDocSection):
                task_list.extendleft(reversed(current.section_contents))

            elif isinstance(current, CompositeRequirement):
                task_list.extendleft(reversed(current.requirements))
